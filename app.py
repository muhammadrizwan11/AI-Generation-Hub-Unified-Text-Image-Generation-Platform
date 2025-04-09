



import streamlit as st
import google.generativeai as genai
import requests
import time
import json
from PIL import Image
from io import BytesIO
import os

class CombinedAIApp:
    def __init__(self):
        # Set page config
        st.set_page_config(
            page_title="Generation Hub",
            page_icon="🤖",
            layout="wide",
            initial_sidebar_state="expanded"
        )
        
        # Add title and description
        st.title("Generation Hub")
        st.markdown("Generate text with prompt")
        
        # API keys hardcoded (not recommended for production)
        self.gemini_api_key = "AIzaSyCzHa6m60yJ6-gd81SABHUrNpK6m3Nl4uY"
        self.starry_api_key = "dugMLMJ_GP-tVeyJE1UIq58ZNQ8-mQ"
        
        # Initialize session state for chat history
        if "gemini_chat_history" not in st.session_state:
            st.session_state.gemini_chat_history = []
            st.session_state.gemini_initialized = False
            st.session_state.generated_image_urls = []
        
        # Create tabs
        tab1, tab2 = st.tabs(["Text Generation", "Image Generation"])
        
        # Build UI for each tab
        with tab1:
            self.build_text_generation_tab()
        
        with tab2:
            self.build_image_generation_tab()
    
    def initialize_gemini(self):
        """Initialize Gemini API and chat"""
        if not st.session_state.gemini_initialized and self.gemini_api_key:
            try:
                genai.configure(api_key=self.gemini_api_key)
                st.session_state.gemini_model = genai.GenerativeModel('gemini-2.0-flash')
                st.session_state.gemini_chat = st.session_state.gemini_model.start_chat(history=[])
                st.session_state.gemini_initialized = True
                
                # Add welcome message if no history
                if not st.session_state.gemini_chat_history:
                    st.session_state.gemini_chat_history.append({
                        "role": "assistant",
                        "content": "Hello! How can I assist you today?"
                    })
                
                return True
            except Exception as e:
                st.error(f"Error initializing Gemini API: {str(e)}")
                return False
        return st.session_state.gemini_initialized
    
    def build_text_generation_tab(self):
        """Build the text generation tab UI"""
        st.header("Text Generation")
        
        # Chat container to display messages
        chat_container = st.container()
        
        # Display chat history
        with chat_container:
            for message in st.session_state.gemini_chat_history:
                if message["role"] == "user":
                    st.chat_message("user").write(message["content"])
                else:
                    st.chat_message("assistant").write(message["content"])
        
        # Input for user message
        user_message = st.chat_input("Type your message here...")
        
        # Process user input
        if user_message:
            # Add user message to chat history
            st.session_state.gemini_chat_history.append({
                "role": "user",
                "content": user_message
            })
            
            # Display user message
            with chat_container:
                st.chat_message("user").write(user_message)
            
            # Initialize Gemini if needed
            if self.initialize_gemini():
                with st.spinner("Thinking..."):
                    try:
                        # Get response from Gemini
                        response = st.session_state.gemini_chat.send_message(user_message)
                        response_text = response.text
                        
                        # Add AI response to chat history
                        st.session_state.gemini_chat_history.append({
                            "role": "assistant",
                            "content": response_text
                        })
                        
                        # Display AI response
                        with chat_container:
                            st.chat_message("assistant").write(response_text)
                    
                    except Exception as e:
                        error_message = f"An error occurred: {str(e)}"
                        st.error(error_message)
                        
                        # Add error to chat history
                        st.session_state.gemini_chat_history.append({
                            "role": "assistant",
                            "content": error_message
                        })
        
        # Clear chat button
        if st.button("Clear Chat History", key="clear_chat"):
            st.session_state.gemini_chat_history = []
            if st.session_state.gemini_initialized:
                st.session_state.gemini_chat = st.session_state.gemini_model.start_chat(history=[])
            st.session_state.gemini_chat_history.append({
                "role": "assistant",
                "content": "Chat history cleared. How can I assist you?"
            })
            st.rerun()
    
    def build_image_generation_tab(self):
        """Build the image generation tab UI"""
        st.header("Image Generation")
        
        # Create two columns for input and options
        col1, col2 = st.columns([3, 2])
        
        # Prompt input
        with col1:
            prompt = st.text_area("Enter your prompt:", height=100)
            
            if st.button("Generate Images", key="generate_image"):
                if not prompt.strip():
                    st.error("Please enter a prompt")
                elif not self.starry_api_key:
                    st.error("Please enter your StarryAI API key")
                else:
                    # Clear previous images
                    st.session_state.generated_image_urls = []
                    
                    # Start generation process
                    with st.spinner("Generating images..."):
                        self.generate_images(prompt)
        
        # Options
        with col2:
            st.subheader("Options")
            model = st.selectbox("Model", ["lyra"], index=0)
            aspect_ratio = st.selectbox("Aspect Ratio", ["square", "portrait", "landscape"], index=0)
            high_res = st.checkbox("High Resolution", value=False)
            steps = st.slider("Steps", min_value=5, max_value=50, value=20)
            num_images = st.slider("Number of Images", min_value=1, max_value=4, value=4)
            
            # Store options in session state
            st.session_state.image_options = {
                "model": model,
                "aspect_ratio": aspect_ratio,
                "high_res": high_res,
                "steps": steps,
                "num_images": num_images
            }
        
        # Display area for generated images
        if st.session_state.generated_image_urls:
            st.subheader("Generated Images")
            
            # Create a grid for images (2 columns)
            cols = st.columns(2)
            
            for i, url in enumerate(st.session_state.generated_image_urls):
                col_index = i % 2
                
                with cols[col_index]:
                    try:
                        # Display image
                        response = requests.get(url)
                        if response.status_code == 200:
                            img = Image.open(BytesIO(response.content))
                            st.image(img, caption=f"Image {i+1}", use_container_width=True)
                            
                            # Add download button
                            img_bytes = BytesIO()
                            img.save(img_bytes, format="PNG")
                            st.download_button(
                                label="Download Image",
                                data=img_bytes.getvalue(),
                                file_name=f"ai_generated_{int(time.time())}_{i+1}.png",
                                mime="image/png"
                            )
                        else:
                            st.error(f"Could not load image {i+1}")
                    
                    except Exception as e:
                        st.error(f"Error displaying image {i+1}: {str(e)}")
        
        # Log area
        if "image_log" in st.session_state and st.session_state.image_log:
            st.subheader("Generation Log")
            st.text_area("Log", value=st.session_state.image_log, height=200, disabled=True)
    
    def generate_images(self, prompt):
        """Generate images using StarryAI API"""
        try:
            # Initialize log in session state if not exists
            if "image_log" not in st.session_state:
                st.session_state.image_log = ""
            
            # Log function
            def log(message):
                st.session_state.image_log = f"{st.session_state.image_log}\n{message}"
            
            log(f"Starting image generation with prompt: '{prompt}'")
            
            # Get parameters from session state
            options = st.session_state.image_options
            model = options["model"]
            aspect_ratio = options["aspect_ratio"]
            high_res = options["high_res"]
            steps = options["steps"]
            num_images = options["num_images"]
            
            # API call parameters
            url = "https://api.starryai.com/creations/"
            payload = {
                "prompt": prompt,
                "model": model,
                "aspectRatio": aspect_ratio,
                "highResolution": high_res,
                "images": num_images,
                "steps": steps,
                "initialImageMode": "color"
            }
            headers = {
                "accept": "application/json",
                "content-type": "application/json",
                "X-API-Key": self.starry_api_key
            }
            
            # Make API request
            log("Sending request to StarryAI API...")
            response = requests.post(url, json=payload, headers=headers)
            
            log(f"Response status code: {response.status_code}")
            
            if response.status_code != 200:
                log(f"Error: API returned status code {response.status_code}")
                log(f"Response content: {response.text}")
                st.error(f"API Error: {response.text}")
                return
            
            # Parse response
            try:
                creation_data = response.json()
                creation_id = creation_data.get('id')
                log(f"Creation started with ID: {creation_id}")
                
                # Wait for creation to complete
                self.wait_for_creation(creation_id, log)
                
            except json.JSONDecodeError:
                log("Error: Could not parse JSON response")
                st.error("Could not parse API response")
        
        except Exception as e:
            if "image_log" in st.session_state:
                st.session_state.image_log += f"\nError during generation: {str(e)}"
            st.error(f"Error during image generation: {str(e)}")
    
    def wait_for_creation(self, creation_id, log_func, max_wait_time=300, check_interval=5):
        """Wait for an image creation to complete"""
        start_time = time.time()
        progress_bar = st.progress(0)
        
        while time.time() - start_time < max_wait_time:
            # Update progress bar (approximate)
            elapsed = time.time() - start_time
            progress = min(elapsed / max_wait_time, 0.95)
            progress_bar.progress(progress)
            
            log_func(f"Checking status of creation {creation_id}...")
            
            # Check status
            url = f"https://api.starryai.com/creations/{creation_id}"
            headers = {
                "accept": "application/json",
                "X-API-Key": self.starry_api_key
            }
            
            response = requests.get(url, headers=headers)
            
            if response.status_code != 200:
                log_func(f"Error checking status: API returned status code {response.status_code}")
                log_func(f"Response: {response.text}")
                st.error(f"Error checking status: {response.text}")
                return
            
            try:
                status_data = response.json()
                status = status_data.get("status")
                log_func(f"Current status: {status}")
                
                if status == "completed":
                    # Process completed images
                    progress_bar.progress(1.0)
                    self.process_completed_images(status_data, log_func)
                    return
                elif status == "failed":
                    log_func("Creation failed")
                    st.error("Image creation failed")
                    return
                
                log_func(f"Waiting {check_interval} seconds before checking again...")
                time.sleep(check_interval)
                
            except json.JSONDecodeError:
                log_func("Error: Could not parse JSON response")
                st.error("Could not parse API response")
                return
        
        log_func(f"Timed out after {max_wait_time} seconds")
        st.error(f"Image generation timed out after {max_wait_time} seconds")
    
    def process_completed_images(self, completed_data, log_func):
        """Process completed images"""
        if "images" not in completed_data or not completed_data["images"]:
            log_func("No images found in completed data")
            st.error("No images were generated")
            return
        
        images = completed_data["images"]
        log_func(f"Found {len(images)} generated images")
        
        # Store image URLs in session state
        st.session_state.generated_image_urls = [img["url"] for img in images if img.get("url")]
        log_func(f"Image generation complete! {len(st.session_state.generated_image_urls)} images are ready.")
        
        # Success message
        st.success(f"Successfully generated {len(st.session_state.generated_image_urls)} images!")


if __name__ == "__main__":
    app = CombinedAIApp()
