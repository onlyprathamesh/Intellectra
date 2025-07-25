import streamlit as st
import sys
import os
from io import StringIO
import contextlib
from pathlib import Path
# from main import Intellectra  # Import your existing Intellectra class - COMMENTED OUT
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

# Sidebar for configuration (optional)
with st.sidebar:
    st.header("Configuration")
    st.info("Configure your CrewAI execution settings here")
    
    # You can add more configuration options here
    show_logs = st.checkbox("Show execution logs", value=False)
    auto_scroll = st.checkbox("Auto-scroll logs", value=True)

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
            # Add more inputs as needed
        }
        
        # Create containers for output
        status_container = st.container()
        logs_container = st.container() if show_logs else None
        results_container = st.container()
        
        with status_container:
            st.info("🔄 Loading results... Please wait.")
            progress_bar = st.progress(0)
            status_text = st.empty()
        
        try:
            # Update progress
            progress_bar.progress(25)
            status_text.text("Reading summarizer output...")
            
            # COMMENTED OUT: CrewAI execution
            # # Capture stdout for logs only if show_logs is enabled
            # if show_logs:
            #     old_stdout = sys.stdout
            #     sys.stdout = captured_output = StringIO()
            # 
            # # Update progress
            # progress_bar.progress(25)
            # status_text.text("Initializing CrewAI...")
            # 
            # # Run the crew
            # progress_bar.progress(50)
            # status_text.text("Executing agents...")
            # 
            # # Your main execution
            # result = Intellectra().crew().kickoff(inputs=inputs)
            # 
            # progress_bar.progress(75)
            # status_text.text("Processing results...")
            
            # Read summarizer output directly
            progress_bar.progress(50)
            status_text.text("Loading summary report...")
            
            summarizer_content = read_summarizer_output()
            
            progress_bar.progress(100)
            status_text.text("✅ Loading completed!")
            
            # COMMENTED OUT: Log restoration
            # # Restore stdout and show logs if enabled
            # if show_logs:
            #     sys.stdout = old_stdout
            #     captured_logs = captured_output.getvalue()
            #     
            #     if logs_container:
            #         with log_placeholder.container():
            #             if captured_logs:
            #                 st.code(captured_logs, language="text")
            #             else:
            #                 st.text("No logs captured during execution.")
            
            # Display results
            with results_container:
                st.success("🎉 Summary report loaded successfully!")
                
                # Show summarizer output if available
                if summarizer_content:
                    st.subheader("📋 Summary Report")
                    
                    # Display the markdown content
                    st.markdown(summarizer_content)
                    
                    # Download option for summary
                    st.download_button(
                        label="📥 Download Summary Report",
                        data=summarizer_content,
                        file_name="summarizer_output.md",
                        mime="text/markdown"
                    )
                else:
                    st.warning("📄 Summarizer output file not found at outputs/summarizer_output.md")
                    st.info("Please ensure the summarizer_output.md file exists in the outputs folder.")
                
                # COMMENTED OUT: Additional results section
                # # Show additional results in an expander (optional)
                # with st.expander("Additional Results", expanded=False):
                #     # Display the result based on its type
                #     if hasattr(result, 'raw'):
                #         st.markdown("**Raw Output:**")
                #         st.write(result.raw)
                #     
                #     if hasattr(result, 'json_dict'):
                #         st.markdown("**Structured Output:**")
                #         st.json(result.json_dict)
                #     
                #     if hasattr(result, 'tasks_output'):
                #         st.markdown("**Task Outputs:**")
                #         for i, task_output in enumerate(result.tasks_output):
                #             with st.expander(f"Task {i+1} Output", expanded=False):
                #                 st.write(task_output.raw if hasattr(task_output, 'raw') else str(task_output))
                #     
                #     # If result is a simple string or other type
                #     if isinstance(result, (str, dict, list)):
                #         st.write(result)
                #     
                #     # Download results option for raw data
                #     if hasattr(result, 'raw') and result.raw:
                #         st.download_button(
                #             label="📥 Download Raw Results",
                #             data=result.raw,
                #             file_name="crewai_raw_results.txt",
                #             mime="text/plain"
                #         )
        
        except Exception as e:
            # COMMENTED OUT: Stdout restoration in error case
            # # Restore stdout in case of error
            # if show_logs and 'old_stdout' in locals():
            #     sys.stdout = old_stdout
            
            progress_bar.progress(0)
            status_text.text("")
            
            st.error(f"❌ An error occurred while loading the summary: {str(e)}")
            
            # Show error details in an expander
            with st.expander("Error Details", expanded=False):
                st.code(str(e), language="python")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: #666;'>
        Built with ❤️ using Streamlit and CrewAI
    </div>
    """,
    unsafe_allow_html=True
)