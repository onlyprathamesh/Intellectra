import streamlit as st
import sys
import os
from io import StringIO
import contextlib
from pathlib import Path
from main import Intellectra  # Import your existing Intellectra class
from dotenv import load_dotenv
load_dotenv()

# Set page configuration
st.set_page_config(
    page_title="CrewAI Intellectra Platform",
    page_icon="🤖",
    layout="wide"
)

# Title and description
st.title("🤖 CrewAI Intellectra Platform")
st.markdown("---")

# Sidebar for configuration
with st.sidebar:
    st.header("Configuration")
    st.info("Configure your CrewAI execution settings here")
    
    # Configuration options
    show_logs = st.checkbox("Show execution logs", value=False)
    auto_scroll = st.checkbox("Auto-scroll logs", value=True)
    show_raw_output = st.checkbox("Show raw output", value=True)
    show_task_outputs = st.checkbox("Show individual task outputs", value=False)

# Main input section
st.header("Problem Statement Input")
problem_statement = st.text_area(
    "Enter your problem statement:",
    value="Built an RAG platform for Q&A",
    height=100,
    help="Describe the problem you want the CrewAI agents to work on"
)

# Run button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    run_button = st.button("🚀 Run CrewAI", use_container_width=True, type="primary")

# Helper function to read summarizer output
def read_summarizer_output():
    """Read the summarizer_output.md file from outputs folder"""
    try:
        output_path = Path("outputs/summarizer_output.md")
        if output_path.exists():
            with open(output_path, 'r', encoding='utf-8') as f:
                return f.read()
        else:
            return None
    except Exception as e:
        st.error(f"Error reading summarizer output: {str(e)}")
        return None

# Results section
if run_button:
    if not problem_statement.strip():
        st.error("Please enter a problem statement before running.")
    else:
        # Create inputs dictionary
        inputs = {
            'problem_statement': problem_statement,
        }
        
        # Create containers for output
        status_container = st.container()
        logs_container = st.container() if show_logs else None
        results_container = st.container()
        
        with status_container:
            st.info("🔄 Initializing CrewAI execution... Please wait.")
            progress_bar = st.progress(0)
            status_text = st.empty()
        
        # Create log placeholder if logs are enabled
        if show_logs:
            with logs_container:
                st.subheader("📊 Execution Logs")
                log_placeholder = st.empty()
        
        try:
            # Capture stdout for logs if enabled
            if show_logs:
                old_stdout = sys.stdout
                sys.stdout = captured_output = StringIO()
            
            # Update progress
            progress_bar.progress(25)
            status_text.text("Initializing CrewAI...")
            
            # Initialize Intellectra
            intellectra = Intellectra()
            crew = intellectra.crew()
            
            # Update progress
            progress_bar.progress(50)
            status_text.text("Executing agents...")
            
            # Run the crew
            result = crew.kickoff(inputs=inputs)
            
            progress_bar.progress(75)
            status_text.text("Processing results...")
            
            # Read summarizer output
            summarizer_content = read_summarizer_output()
            
            progress_bar.progress(100)
            status_text.text("✅ Execution completed!")
            
            # Restore stdout and show logs if enabled
            if show_logs:
                sys.stdout = old_stdout
                captured_logs = captured_output.getvalue()
                
                if logs_container:
                    with log_placeholder.container():
                        if captured_logs:
                            st.code(captured_logs, language="text")
                        else:
                            st.text("No logs captured during execution.")
            
            # Display results
            with results_container:
                st.success("🎉 CrewAI execution completed successfully!")
                
                # Show summarizer output if available
                if summarizer_content:
                    st.subheader("📋 Summary Report")
                    st.markdown(summarizer_content)
                    
                    # Download option for summary
                    st.download_button(
                        label="📥 Download Summary Report",
                        data=summarizer_content,
                        file_name="summarizer_output.md",
                        mime="text/markdown"
                    )
                
                # Show main crew results
                st.subheader("🔍 CrewAI Results")
                
                # Display raw output if enabled and available
                if show_raw_output and hasattr(result, 'raw') and result.raw:
                    with st.expander("Raw Output", expanded=True):
                        st.markdown("**Complete Raw Output:**")
                        st.write(result.raw)
                        
                        # Download raw results
                        st.download_button(
                            label="📥 Download Raw Results",
                            data=result.raw,
                            file_name="crewai_raw_results.txt",
                            mime="text/plain"
                        )
                
                # Display structured output if available
                if hasattr(result, 'json_dict') and result.json_dict:
                    with st.expander("Structured Output", expanded=False):
                        st.markdown("**JSON Structured Output:**")
                        st.json(result.json_dict)
                
                # Display individual task outputs if enabled
                if show_task_outputs and hasattr(result, 'tasks_output') and result.tasks_output:
                    st.markdown("**Individual Task Outputs:**")
                    for i, task_output in enumerate(result.tasks_output):
                        with st.expander(f"Task {i+1} Output", expanded=False):
                            if hasattr(task_output, 'raw'):
                                st.write(task_output.raw)
                            else:
                                st.write(str(task_output))
                
                # Handle other result types
                if isinstance(result, (str, dict, list)) and not hasattr(result, 'raw'):
                    with st.expander("Result Data", expanded=True):
                        st.write(result)
                
                # Additional information
                if not summarizer_content:
                    st.info("💡 **Note:** Summarizer output file not found. The summary will be generated after crew execution completes.")
                
                # Show success metrics or additional info
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Status", "✅ Completed")
                with col2:
                    if hasattr(result, 'tasks_output'):
                        st.metric("Tasks Executed", len(result.tasks_output))
                    else:
                        st.metric("Tasks Executed", "N/A")
                with col3:
                    st.metric("Result Type", type(result).__name__)
        
        except Exception as e:
            # Restore stdout in case of error
            if show_logs and 'old_stdout' in locals():
                sys.stdout = old_stdout
            
            progress_bar.progress(0)
            status_text.text("")
            
            st.error(f"❌ An error occurred during CrewAI execution: {str(e)}")
            
            # Show error details in an expander
            with st.expander("Error Details", expanded=True):
                st.code(str(e), language="python")
                
                # Additional debugging info
                st.markdown("**Debugging Information:**")
                st.write(f"- Python version: {sys.version}")
                st.write(f"- Current working directory: {os.getcwd()}")
                st.write(f"- Problem statement length: {len(problem_statement)} characters")
                
                # Check if main.py exists
                if not Path("main.py").exists():
                    st.error("⚠️ main.py file not found. Please ensure it exists in the same directory.")
                
                # Check if outputs directory exists
                if not Path("outputs").exists():
                    st.warning("⚠️ outputs directory not found. It will be created during execution.")

# Additional features section
st.markdown("---")
with st.expander("ℹ️ About This Platform", expanded=False):
    st.markdown("""
    ### CrewAI Intellectra Platform
    
    This platform allows you to:
    - Execute CrewAI workflows with custom problem statements
    - View real-time execution logs
    - Download generated reports and outputs
    - Monitor task execution progress
    
    ### Features:
    - **Real-time Logging**: See what your agents are doing in real-time
    - **Multiple Output Formats**: View raw, structured, and summary outputs
    - **Download Results**: Save your results for later analysis
    - **Error Handling**: Comprehensive error reporting and debugging
    
    ### Usage Tips:
    1. Enter a clear, specific problem statement
    2. Enable logs to see detailed execution progress
    3. Use the sidebar options to customize what outputs you want to see
    4. Download results for offline analysis
    """)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666;'>
        Built with ❤️ using Streamlit and CrewAI | Ready for Production Use
    </div>
    """,
    unsafe_allow_html=True
)