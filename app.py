# import tkinter as tk
# from tkinter import scrolledtext, ttk
# import threading
# import google.generativeai as genai
# from PIL import Image, ImageTk
# import os
# import time

# class GeminiChatbot:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Gemini AI Chatbot")
#         self.root.geometry("800x600")
#         self.root.configure(bg="#f0f0f0")
        
#         # Configure API key
#         genai.configure(api_key="AIzaSyCzHa6m60yJ6-gd81SABHUrNpK6m3Nl4uY")
        
#         # Load the model
#         self.model = genai.GenerativeModel('gemini-2.0-flash')
        
#         # Create chat instance
#         self.chat = self.model.start_chat(history=[])
        
#         self.create_widgets()
        
#     def create_widgets(self):
#         # Main frame
#         main_frame = tk.Frame(self.root, bg="#f0f0f0")
#         main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
#         # Chat history area
#         self.chat_history = scrolledtext.ScrolledText(
#             main_frame,
#             wrap=tk.WORD,
#             bg="white",
#             font=("Arial", 10),
#             state="disabled",
#             height=20
#         )
#         self.chat_history.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
#         # Input area frame
#         input_frame = tk.Frame(main_frame, bg="#f0f0f0")
#         input_frame.pack(fill=tk.X, pady=5)
        
#         # Message input field
#         self.message_input = scrolledtext.ScrolledText(
#             input_frame,
#             wrap=tk.WORD,
#             height=3,
#             font=("Arial", 10)
#         )
#         self.message_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
#         self.message_input.bind("<Return>", self.send_on_enter)
        
#         # Send button
#         self.send_button = ttk.Button(
#             input_frame,
#             text="Send",
#             command=self.send_message,
#             style="Send.TButton"
#         )
#         self.send_button.pack(side=tk.RIGHT, padx=5)
        
#         # Status bar
#         self.status_var = tk.StringVar()
#         self.status_var.set("Ready")
#         self.status_bar = tk.Label(
#             self.root,
#             textvariable=self.status_var,
#             bd=1,
#             relief=tk.SUNKEN,
#             anchor=tk.W
#         )
#         self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        
#         # Style configuration
#         style = ttk.Style()
#         style.configure("Send.TButton", font=("Arial", 10, "bold"))
        
#         # Welcome message
#         self.update_chat_history("Gemini AI: Hello! How can I assist you today?", "bot")
        
#     def update_chat_history(self, message, sender):
#         self.chat_history.config(state="normal")
        
#         # Format based on sender
#         if sender == "user":
#             self.chat_history.insert(tk.END, "You: " + message + "\n\n", "user_msg")
#             self.chat_history.tag_config("user_msg", foreground="#0078D7", font=("Arial", 10, "bold"))
#         elif sender == "bot":
#             self.chat_history.insert(tk.END, message + "\n\n", "bot_msg")
#             self.chat_history.tag_config("bot_msg", foreground="#4a4a4a", font=("Arial", 10))
        
#         self.chat_history.config(state="disabled")
#         self.chat_history.see(tk.END)
    
#     def send_on_enter(self, event):
#         if not event.state & 0x0001:  # Check if shift key is not pressed
#             self.send_message()
#             return "break"  # Prevents the default behavior (newline)
    
#     def send_message(self):
#         user_message = self.message_input.get("1.0", tk.END).strip()
#         if not user_message:
#             return
        
#         # Clear input field
#         self.message_input.delete("1.0", tk.END)
        
#         # Update chat history with user message
#         self.update_chat_history(user_message, "user")
        
#         # Disable send button and update status
#         self.send_button.config(state="disabled")
#         self.status_var.set("Thinking...")
#         self.root.update_idletasks()
        
#         # Process in a separate thread to keep UI responsive
#         threading.Thread(target=self.get_ai_response, args=(user_message,), daemon=True).start()
    
#     def get_ai_response(self, user_message):
#         try:
#             # Get response from Gemini
#             response = self.chat.send_message(user_message)
#             response_text = response.text
            
#             # Update the chat history with AI response
#             self.root.after(0, lambda: self.update_chat_history(f"Gemini AI: {response_text}", "bot"))
            
#         except Exception as e:
#             error_message = f"An error occurred: {str(e)}"
#             self.root.after(0, lambda: self.update_chat_history(f"Gemini AI: {error_message}", "bot"))
        
#         # Re-enable the send button and update status
#         self.root.after(0, lambda: self.send_button.config(state="normal"))
#         self.root.after(0, lambda: self.status_var.set("Ready"))

# def main():
#     root = tk.Tk()
#     app = GeminiChatbot(root)
#     root.mainloop()

# if __name__ == "__main__":
#     main()









# import requests
# import json
# import time
# import os

# # Simple StarryAI image generator based on your provided code

# def generate_image(api_key, prompt):
#     """Generate an image using the StarryAI API"""
#     url = "https://api.starryai.com/creations/"
    
#     payload = {
#         "prompt": prompt,
#         "model": "lyra",
#         "aspectRatio": "square",
#         "highResolution": False,
#         "images": 4,
#         "steps": 20,
#         "initialImageMode": "color"
#     }
    
#     headers = {
#         "accept": "application/json",
#         "content-type": "application/json",
#         "X-API-Key": api_key
#     }
    
#     print("Sending request to StarryAI API...")
#     response = requests.post(url, json=payload, headers=headers)
    
#     # Print the raw response for debugging
#     print(f"Response status code: {response.status_code}")
#     print(f"Response content: {response.text}")
    
#     if response.status_code != 200:
#         print(f"Error: API returned status code {response.status_code}")
#         return None
    
#     try:
#         return response.json()
#     except json.JSONDecodeError:
#         print("Error: Could not parse JSON response")
#         return None

# def check_creation_status(api_key, creation_id):
#     """Check the status of an image creation"""
#     url = f"https://api.starryai.com/creations/{creation_id}"
    
#     headers = {
#         "accept": "application/json",
#         "X-API-Key": api_key
#     }
    
#     response = requests.get(url, headers=headers)
    
#     if response.status_code != 200:
#         print(f"Error checking status: API returned status code {response.status_code}")
#         print(f"Response: {response.text}")
#         return None
    
#     try:
#         return response.json()
#     except json.JSONDecodeError:
#         print("Error: Could not parse JSON response")
#         return None

# def wait_for_creation(api_key, creation_id, max_wait_time=300, check_interval=5):
#     """Wait for an image creation to complete"""
#     start_time = time.time()
    
#     while time.time() - start_time < max_wait_time:
#         print(f"Checking status of creation {creation_id}...")
#         status_data = check_creation_status(api_key, creation_id)
        
#         if not status_data:
#             print("Failed to get status data")
#             return None
        
#         print(f"Status data: {json.dumps(status_data, indent=2)}")
        
#         # Extract status from response (adjust based on actual API response structure)
#         status = status_data.get("status")
#         if not status:
#             print("Could not find status in response")
#             return None
        
#         print(f"Current status: {status}")
        
#         if status == "completed":
#             return status_data
#         elif status == "failed":
#             print("Creation failed")
#             return status_data
        
#         print(f"Waiting {check_interval} seconds before checking again...")
#         time.sleep(check_interval)
    
#     print(f"Timed out after {max_wait_time} seconds")
#     return None

# def download_and_save_image(image_url, output_path="generated_image.png"):
#     """Download and save an image from a URL"""
#     try:
#         response = requests.get(image_url)
        
#         if response.status_code != 200:
#             print(f"Error downloading image: API returned status code {response.status_code}")
#             return False
        
#         with open(output_path, "wb") as f:
#             f.write(response.content)
        
#         print(f"Image saved to {output_path}")
#         return True
#     except Exception as e:
#         print(f"Error downloading image: {e}")
#         return False

# def main():
#     # Your API key
#     api_key = "dugMLMJ_GP-tVeyJE1UIq58ZNQ8-mQ"
    
#     # Get prompt from user
#     prompt = input("Enter a prompt for image generation: ")
    
#     # Generate image
#     print(f"Starting image generation with prompt: '{prompt}'")
#     creation_data = generate_image(api_key, prompt)
    
#     if not creation_data:
#         print("Failed to start generation")
#         return
    
#     print(f"API Response: {json.dumps(creation_data, indent=2)}")
    
#     # Extract creation ID (adjust based on actual API response structure)
#     creation_id = creation_data.get("id")
#     if not creation_id:
#         print("No creation ID in response")
#         return
    
#     print(f"Creation started with ID: {creation_id}")
    
#     # Wait for creation to complete
#     print("Waiting for image generation to complete...")
#     completed_data = wait_for_creation(api_key, creation_id)
    
#     if not completed_data:
#         print("Failed to get completed creation data")
#         return
    
#     # Get image URL (adjust based on actual API response structure)
#     # This might be different based on the API's actual response format
#     image_url = None
#     if "imageUrl" in completed_data:
#         image_url = completed_data["imageUrl"]
#     elif "output" in completed_data and "imageUrl" in completed_data["output"]:
#         image_url = completed_data["output"]["imageUrl"]
#     elif "images" in completed_data and len(completed_data["images"]) > 0:
#         image_url = completed_data["images"][0]["url"]
    
#     if not image_url:
#         print("Could not find image URL in response")
#         print(f"Response data: {json.dumps(completed_data, indent=2)}")
#         return
    
#     # Download and save the image
#     output_filename = f"starryai_{int(time.time())}.png"
#     if download_and_save_image(image_url, output_filename):
#         print(f"Successfully generated and saved image to {output_filename}")
        
#         # Try to open the image
#         try:
#             from PIL import Image
#             Image.open(output_filename).show()
#             print("Image opened in default viewer")
#         except ImportError:
#             print("PIL not installed, cannot display image")
#         except Exception as e:
#             print(f"Could not display image: {e}")
#     else:
#         print("Failed to download and save image")

# if __name__ == "__main__":
#     main()





# import tkinter as tk
# from tkinter import ttk, scrolledtext
# import requests
# import json
# import time
# import os
# import threading
# from PIL import Image, ImageTk
# from io import BytesIO
# import webbrowser

# class StarryAIGenerator:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("StarryAI Image Generator")
#         self.root.geometry("1000x800")
#         self.root.configure(bg="#f0f0f0")
        
#         # Your API key - you might want to store this more securely in a real application
#         self.api_key = "dugMLMJ_GP-tVeyJE1UIq58ZNQ8-mQ"
        
#         # Create UI elements
#         self.create_widgets()
        
#         # Store image references to prevent garbage collection
#         self.image_references = []
        
#         # For storing generated image URLs
#         self.generated_image_urls = []
        
#     def create_widgets(self):
#         # Main frame
#         main_frame = ttk.Frame(self.root, padding="10")
#         main_frame.pack(fill=tk.BOTH, expand=True)
        
#         # Title label
#         title_label = ttk.Label(
#             main_frame, 
#             text="StarryAI Image Generator", 
#             font=("Arial", 20, "bold")
#         )
#         title_label.pack(pady=(0, 20))
        
#         # Input frame
#         input_frame = ttk.Frame(main_frame)
#         input_frame.pack(fill=tk.X, pady=10)
        
#         # Prompt label and entry
#         prompt_label = ttk.Label(input_frame, text="Enter your prompt:", font=("Arial", 12))
#         prompt_label.pack(side=tk.LEFT, padx=(0, 10))
        
#         self.prompt_entry = ttk.Entry(input_frame, width=50, font=("Arial", 12))
#         self.prompt_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        
#         # Generate button
#         self.generate_button = ttk.Button(
#             input_frame, 
#             text="Generate Images", 
#             command=self.start_generation
#         )
#         self.generate_button.pack(side=tk.RIGHT)
        
#         # Options frame
#         options_frame = ttk.LabelFrame(main_frame, text="Options", padding="10")
#         options_frame.pack(fill=tk.X, pady=10)
        
#         # Model selection
#         model_label = ttk.Label(options_frame, text="Model:")
#         model_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        
#         self.model_var = tk.StringVar(value="lyra")
#         model_combo = ttk.Combobox(
#             options_frame, 
#             textvariable=self.model_var, 
#             values=["lyra", "orion", "nebula"],
#             state="readonly",
#             width=15
#         )
#         model_combo.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        
#         # Aspect ratio
#         aspect_label = ttk.Label(options_frame, text="Aspect Ratio:")
#         aspect_label.grid(row=0, column=2, sticky=tk.W, padx=5, pady=5)
        
#         self.aspect_var = tk.StringVar(value="square")
#         aspect_combo = ttk.Combobox(
#             options_frame, 
#             textvariable=self.aspect_var, 
#             values=["square", "portrait", "landscape"],
#             state="readonly",
#             width=15
#         )
#         aspect_combo.grid(row=0, column=3, sticky=tk.W, padx=5, pady=5)
        
#         # High resolution
#         self.high_res_var = tk.BooleanVar(value=False)
#         high_res_check = ttk.Checkbutton(
#             options_frame, 
#             text="High Resolution", 
#             variable=self.high_res_var
#         )
#         high_res_check.grid(row=0, column=4, sticky=tk.W, padx=5, pady=5)
        
#         # Steps
#         steps_label = ttk.Label(options_frame, text="Steps:")
#         steps_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        
#         self.steps_var = tk.IntVar(value=20)
#         steps_spin = ttk.Spinbox(
#             options_frame, 
#             from_=5, 
#             to=50, 
#             textvariable=self.steps_var,
#             width=5
#         )
#         steps_spin.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        
#         # Number of images
#         images_label = ttk.Label(options_frame, text="Images:")
#         images_label.grid(row=1, column=2, sticky=tk.W, padx=5, pady=5)
        
#         self.images_var = tk.IntVar(value=4)
#         images_spin = ttk.Spinbox(
#             options_frame, 
#             from_=1, 
#             to=4, 
#             textvariable=self.images_var,
#             width=5
#         )
#         images_spin.grid(row=1, column=3, sticky=tk.W, padx=5, pady=5)
        
#         # Progress frame
#         progress_frame = ttk.LabelFrame(main_frame, text="Progress", padding="10")
#         progress_frame.pack(fill=tk.X, pady=10)
        
#         # Status label
#         self.status_var = tk.StringVar(value="Ready")
#         status_label = ttk.Label(progress_frame, textvariable=self.status_var)
#         status_label.pack(side=tk.LEFT, padx=(0, 10))
        
#         # Progress bar
#         self.progress = ttk.Progressbar(progress_frame, mode="indeterminate", length=300)
#         self.progress.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
#         # Log frame
#         log_frame = ttk.LabelFrame(main_frame, text="Log", padding="10")
#         log_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
#         # Log text area
#         self.log_text = scrolledtext.ScrolledText(log_frame, height=5, wrap=tk.WORD)
#         self.log_text.pack(fill=tk.BOTH, expand=True)
        
#         # Images frame
#         self.images_frame = ttk.LabelFrame(main_frame, text="Generated Images", padding="10")
#         self.images_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
#         # Image display area
#         self.images_display = ttk.Frame(self.images_frame)
#         self.images_display.pack(fill=tk.BOTH, expand=True)
    
#     def log(self, message):
#         """Add message to log text area"""
#         self.log_text.configure(state="normal")
#         self.log_text.insert(tk.END, message + "\n")
#         self.log_text.see(tk.END)
#         self.log_text.configure(state="disabled")
#         self.root.update_idletasks()
    
#     def start_generation(self):
#         """Start image generation in a separate thread"""
#         prompt = self.prompt_entry.get().strip()
#         if not prompt:
#             self.log("Please enter a prompt")
#             return
        
#         # Disable the generate button and start progress bar
#         self.generate_button.configure(state="disabled")
#         self.progress.start()
#         self.status_var.set("Generating...")
        
#         # Clear previous images
#         for widget in self.images_display.winfo_children():
#             widget.destroy()
#         self.image_references.clear()
#         self.generated_image_urls.clear()
        
#         # Start generation in a new thread
#         thread = threading.Thread(target=self.generate_images, args=(prompt,))
#         thread.daemon = True
#         thread.start()
    
#     def generate_images(self, prompt):
#         """Generate images in a background thread"""
#         try:
#             self.log(f"Starting image generation with prompt: '{prompt}'")
            
#             # Get parameters from UI
#             model = self.model_var.get()
#             aspect_ratio = self.aspect_var.get()
#             high_res = self.high_res_var.get()
#             steps = self.steps_var.get()
#             num_images = self.images_var.get()
            
#             # API call parameters
#             url = "https://api.starryai.com/creations/"
#             payload = {
#                 "prompt": prompt,
#                 "model": model,
#                 "aspectRatio": aspect_ratio,
#                 "highResolution": high_res,
#                 "images": num_images,
#                 "steps": steps,
#                 "initialImageMode": "color"
#             }
#             headers = {
#                 "accept": "application/json",
#                 "content-type": "application/json",
#                 "X-API-Key": self.api_key
#             }
            
#             # Make API request
#             self.log("Sending request to StarryAI API...")
#             response = requests.post(url, json=payload, headers=headers)
            
#             self.log(f"Response status code: {response.status_code}")
            
#             if response.status_code != 200:
#                 self.log(f"Error: API returned status code {response.status_code}")
#                 self.log(f"Response content: {response.text}")
#                 self.root.after(0, self.end_generation)
#                 return
            
#             # Parse response
#             try:
#                 creation_data = response.json()
#                 self.log(f"Creation started with ID: {creation_data.get('id')}")
                
#                 # Wait for creation to complete
#                 self.wait_for_creation(creation_data.get('id'))
                
#             except json.JSONDecodeError:
#                 self.log("Error: Could not parse JSON response")
#                 self.root.after(0, self.end_generation)
        
#         except Exception as e:
#             self.log(f"Error during generation: {str(e)}")
#             self.root.after(0, self.end_generation)
    
#     def wait_for_creation(self, creation_id, max_wait_time=300, check_interval=5):
#         """Wait for an image creation to complete"""
#         start_time = time.time()
        
#         while time.time() - start_time < max_wait_time:
#             self.log(f"Checking status of creation {creation_id}...")
            
#             # Check status
#             url = f"https://api.starryai.com/creations/{creation_id}"
#             headers = {
#                 "accept": "application/json",
#                 "X-API-Key": self.api_key
#             }
            
#             response = requests.get(url, headers=headers)
            
#             if response.status_code != 200:
#                 self.log(f"Error checking status: API returned status code {response.status_code}")
#                 self.log(f"Response: {response.text}")
#                 self.root.after(0, self.end_generation)
#                 return
            
#             try:
#                 status_data = response.json()
#                 status = status_data.get("status")
#                 self.log(f"Current status: {status}")
                
#                 if status == "completed":
#                     # Process completed images
#                     self.process_completed_images(status_data)
#                     return
#                 elif status == "failed":
#                     self.log("Creation failed")
#                     self.root.after(0, self.end_generation)
#                     return
                
#                 self.log(f"Waiting {check_interval} seconds before checking again...")
#                 time.sleep(check_interval)
                
#             except json.JSONDecodeError:
#                 self.log("Error: Could not parse JSON response")
#                 self.root.after(0, self.end_generation)
#                 return
        
#         self.log(f"Timed out after {max_wait_time} seconds")
#         self.root.after(0, self.end_generation)
    
#     def process_completed_images(self, completed_data):
#         """Process and display completed images"""
#         if "images" not in completed_data or not completed_data["images"]:
#             self.log("No images found in completed data")
#             self.root.after(0, self.end_generation)
#             return
        
#         images = completed_data["images"]
#         self.log(f"Found {len(images)} generated images")
        
#         # Store image URLs
#         self.generated_image_urls = [img["url"] for img in images if img.get("url")]
        
#         # Display images
#         self.root.after(0, lambda: self.display_images(self.generated_image_urls))
    
#     def display_images(self, image_urls):
#         """Display images in the UI"""
#         try:
#             # Create frame for image grid
#             image_grid = ttk.Frame(self.images_display)
#             image_grid.pack(fill=tk.BOTH, expand=True)
            
#             # Calculate grid dimensions
#             num_images = len(image_urls)
#             cols = min(2, num_images)  # Max 2 columns
#             rows = (num_images + cols - 1) // cols
            
#             # Download and display each image
#             for i, url in enumerate(image_urls):
#                 # Calculate grid position
#                 row = i // cols
#                 col = i % cols
                
#                 # Create frame for this image
#                 img_frame = ttk.Frame(image_grid, padding=5)
#                 img_frame.grid(row=row, column=col, padx=5, pady=5, sticky=tk.NSEW)
                
#                 # Add placeholder while loading
#                 placeholder_label = ttk.Label(img_frame, text="Loading image...", font=("Arial", 12))
#                 placeholder_label.pack(padx=5, pady=5)
                
#                 # Start a thread to download the image
#                 thread = threading.Thread(
#                     target=self.load_image_thread,
#                     args=(url, img_frame, placeholder_label, i)
#                 )
#                 thread.daemon = True
#                 thread.start()
            
#             # Configure grid weights
#             for i in range(rows):
#                 image_grid.rowconfigure(i, weight=1)
#             for i in range(cols):
#                 image_grid.columnconfigure(i, weight=1)
                
#         except Exception as e:
#             self.log(f"Error displaying images: {str(e)}")
        
#         finally:
#             # End generation process
#             self.end_generation()
    
#     def load_image_thread(self, url, frame, placeholder_label, index):
#         """Thread function to load an image from URL"""
#         try:
#             # Download the image
#             response = requests.get(url)
#             if response.status_code != 200:
#                 self.root.after(0, lambda: self.log(f"Error downloading image {index+1}: Status code {response.status_code}"))
#                 return
            
#             # Create PIL Image from bytes
#             img = Image.open(BytesIO(response.content))
            
#             # Resize for display (maintaining aspect ratio)
#             target_size = 300  # Target size for display
#             ratio = min(target_size / img.width, target_size / img.height)
#             new_size = (int(img.width * ratio), int(img.height * ratio))
#             img_resized = img.resize(new_size, Image.Resampling.LANCZOS)
            
#             # Convert to PhotoImage
#             photo = ImageTk.PhotoImage(img_resized)
#             self.image_references.append(photo)  # Keep a reference
            
#             # Remove placeholder and display image
#             self.root.after(0, lambda: placeholder_label.pack_forget())
            
#             # Create and display the image label
#             image_label = ttk.Label(frame, image=photo)
#             self.root.after(0, lambda: image_label.pack(padx=5, pady=5))
            
#             # Add URL label and save button
#             url_text = f"Image {index+1}"
#             url_label = ttk.Label(frame, text=url_text, cursor="hand2")
#             url_label.bind("<Button-1>", lambda e, u=url: webbrowser.open(u))
#             self.root.after(0, lambda: url_label.pack(padx=5, pady=(0, 5)))
            
#             # Add save button
#             save_button = ttk.Button(
#                 frame, 
#                 text="Save Image", 
#                 command=lambda u=url, i=index: self.save_image(u, i)
#             )
#             self.root.after(0, lambda: save_button.pack(padx=5, pady=5))
            
#         except Exception as e:
#             self.root.after(0, lambda: self.log(f"Error loading image {index+1}: {str(e)}"))
    
#     def save_image(self, url, index):
#         """Save an image to disk"""
#         try:
#             # Download the image
#             response = requests.get(url)
#             if response.status_code != 200:
#                 self.log(f"Error downloading image for saving: Status code {response.status_code}")
#                 return
            
#             # Create a unique filename
#             output_filename = f"starryai_{int(time.time())}_{index+1}.png"
            
#             # Save the image
#             with open(output_filename, "wb") as f:
#                 f.write(response.content)
                
#             self.log(f"Image saved to {output_filename}")
            
#         except Exception as e:
#             self.log(f"Error saving image: {str(e)}")
    
#     def end_generation(self):
#         """End the generation process, reset UI"""
#         self.generate_button.configure(state="normal")
#         self.progress.stop()
#         self.status_var.set("Ready")

# def main():
#     root = tk.Tk()
#     app = StarryAIGenerator(root)
#     root.mainloop()

# if __name__ == "__main__":
#     main()














# import tkinter as tk
# from tkinter import ttk, scrolledtext, filedialog
# import requests
# import json
# import time
# import os
# import threading
# from PIL import Image, ImageTk
# from io import BytesIO
# import webbrowser

# class StarryAIGenerator:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("StarryAI Image Generator")
#         self.root.geometry("1000x800")
#         self.root.configure(bg="#f0f0f0")
        
#         # Your API key - you might want to store this more securely in a real application
#         self.api_key = "dugMLMJ_GP-tVeyJE1UIq58ZNQ8-mQ"
        
#         # Create UI elements
#         self.create_widgets()
        
#         # Store image references to prevent garbage collection
#         self.image_references = []
        
#         # For storing generated image URLs
#         self.generated_image_urls = []
        
#     def create_widgets(self):
#         # Main frame
#         main_frame = ttk.Frame(self.root, padding="10")
#         main_frame.pack(fill=tk.BOTH, expand=True)
        
#         # Title label
#         title_label = ttk.Label(
#             main_frame, 
#             text="StarryAI Image Generator", 
#             font=("Arial", 20, "bold")
#         )
#         title_label.pack(pady=(0, 20))
        
#         # Input frame
#         input_frame = ttk.Frame(main_frame)
#         input_frame.pack(fill=tk.X, pady=10)
        
#         # Prompt label and entry
#         prompt_label = ttk.Label(input_frame, text="Enter your prompt:", font=("Arial", 12))
#         prompt_label.pack(side=tk.LEFT, padx=(0, 10))
        
#         self.prompt_entry = ttk.Entry(input_frame, width=50, font=("Arial", 12))
#         self.prompt_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
        
#         # Generate button
#         self.generate_button = ttk.Button(
#             input_frame, 
#             text="Generate Images", 
#             command=self.start_generation
#         )
#         self.generate_button.pack(side=tk.RIGHT)
        
#         # Options frame
#         options_frame = ttk.LabelFrame(main_frame, text="Options", padding="10")
#         options_frame.pack(fill=tk.X, pady=10)
        
#         # Model selection
#         model_label = ttk.Label(options_frame, text="Model:")
#         model_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        
#         self.model_var = tk.StringVar(value="lyra")
#         model_combo = ttk.Combobox(
#             options_frame, 
#             textvariable=self.model_var, 
#             values=["lyra"],
#             state="readonly",
#             width=15
#         )
#         model_combo.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
        
#         # Aspect ratio
#         aspect_label = ttk.Label(options_frame, text="Aspect Ratio:")
#         aspect_label.grid(row=0, column=2, sticky=tk.W, padx=5, pady=5)
        
#         self.aspect_var = tk.StringVar(value="square")
#         aspect_combo = ttk.Combobox(
#             options_frame, 
#             textvariable=self.aspect_var, 
#             values=["square", "portrait", "landscape"],
#             state="readonly",
#             width=15
#         )
#         aspect_combo.grid(row=0, column=3, sticky=tk.W, padx=5, pady=5)
        
#         # High resolution
#         self.high_res_var = tk.BooleanVar(value=False)
#         high_res_check = ttk.Checkbutton(
#             options_frame, 
#             text="High Resolution", 
#             variable=self.high_res_var
#         )
#         high_res_check.grid(row=0, column=4, sticky=tk.W, padx=5, pady=5)
        
#         # Steps
#         steps_label = ttk.Label(options_frame, text="Steps:")
#         steps_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        
#         self.steps_var = tk.IntVar(value=20)
#         steps_spin = ttk.Spinbox(
#             options_frame, 
#             from_=5, 
#             to=50, 
#             textvariable=self.steps_var,
#             width=5
#         )
#         steps_spin.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
        
#         # Number of images
#         images_label = ttk.Label(options_frame, text="Images:")
#         images_label.grid(row=1, column=2, sticky=tk.W, padx=5, pady=5)
        
#         self.images_var = tk.IntVar(value=4)
#         images_spin = ttk.Spinbox(
#             options_frame, 
#             from_=1, 
#             to=4, 
#             textvariable=self.images_var,
#             width=5
#         )
#         images_spin.grid(row=1, column=3, sticky=tk.W, padx=5, pady=5)
        
#         # Progress frame
#         progress_frame = ttk.LabelFrame(main_frame, text="Progress", padding="10")
#         progress_frame.pack(fill=tk.X, pady=10)
        
#         # Status label
#         self.status_var = tk.StringVar(value="Ready")
#         status_label = ttk.Label(progress_frame, textvariable=self.status_var)
#         status_label.pack(side=tk.LEFT, padx=(0, 10))
        
#         # Progress bar
#         self.progress = ttk.Progressbar(progress_frame, mode="indeterminate", length=300)
#         self.progress.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
#         # Log frame
#         log_frame = ttk.LabelFrame(main_frame, text="Log", padding="10")
#         log_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
#         # Log text area
#         self.log_text = scrolledtext.ScrolledText(log_frame, height=5, wrap=tk.WORD)
#         self.log_text.pack(fill=tk.BOTH, expand=True)
        
#         # Images frame with scrolling capability
#         images_outer_frame = ttk.LabelFrame(main_frame, text="Generated Images", padding="10")
#         images_outer_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
#         # Add a canvas with scrollbar for image display
#         self.images_canvas = tk.Canvas(images_outer_frame)
#         scrollbar = ttk.Scrollbar(images_outer_frame, orient="vertical", command=self.images_canvas.yview)
#         self.images_frame = ttk.Frame(self.images_canvas)
        
#         # Configure the canvas
#         self.images_canvas.configure(yscrollcommand=scrollbar.set)
#         scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
#         self.images_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
#         # Create window in canvas for the images frame
#         self.canvas_frame = self.images_canvas.create_window((0, 0), window=self.images_frame, anchor="nw")
        
#         # Configure canvas scrolling
#         self.images_frame.bind("<Configure>", self.on_frame_configure)
#         self.images_canvas.bind("<Configure>", self.on_canvas_configure)
        
#         # Bind mousewheel for scrolling
#         self.images_canvas.bind_all("<MouseWheel>", self.on_mousewheel)
    
#     def on_frame_configure(self, event):
#         """Reset the scroll region to encompass the inner frame"""
#         self.images_canvas.configure(scrollregion=self.images_canvas.bbox("all"))
    
#     def on_canvas_configure(self, event):
#         """When canvas is resized, update the window size"""
#         canvas_width = event.width
#         self.images_canvas.itemconfig(self.canvas_frame, width=canvas_width)
    
#     def on_mousewheel(self, event):
#         """Handle mousewheel scrolling"""
#         self.images_canvas.yview_scroll(int(-1*(event.delta/120)), "units")
    
#     def log(self, message):
#         """Add message to log text area"""
#         self.log_text.configure(state="normal")
#         self.log_text.insert(tk.END, message + "\n")
#         self.log_text.see(tk.END)
#         self.log_text.configure(state="disabled")
#         self.root.update_idletasks()
    
#     def start_generation(self):
#         """Start image generation in a separate thread"""
#         prompt = self.prompt_entry.get().strip()
#         if not prompt:
#             self.log("Please enter a prompt")
#             return
        
#         # Disable the generate button and start progress bar
#         self.generate_button.configure(state="disabled")
#         self.progress.start()
#         self.status_var.set("Generating...")
        
#         # Clear previous images
#         for widget in self.images_frame.winfo_children():
#             widget.destroy()
#         self.image_references.clear()
#         self.generated_image_urls.clear()
        
#         # Start generation in a new thread
#         thread = threading.Thread(target=self.generate_images, args=(prompt,))
#         thread.daemon = True
#         thread.start()
    
#     def generate_images(self, prompt):
#         """Generate images in a background thread"""
#         try:
#             self.log(f"Starting image generation with prompt: '{prompt}'")
            
#             # Get parameters from UI
#             model = self.model_var.get()
#             aspect_ratio = self.aspect_var.get()
#             high_res = self.high_res_var.get()
#             steps = self.steps_var.get()
#             num_images = self.images_var.get()
            
#             # API call parameters
#             url = "https://api.starryai.com/creations/"
#             payload = {
#                 "prompt": prompt,
#                 "model": model,
#                 "aspectRatio": aspect_ratio,
#                 "highResolution": high_res,
#                 "images": num_images,
#                 "steps": steps,
#                 "initialImageMode": "color"
#             }
#             headers = {
#                 "accept": "application/json",
#                 "content-type": "application/json",
#                 "X-API-Key": self.api_key
#             }
            
#             # Make API request
#             self.log("Sending request to StarryAI API...")
#             response = requests.post(url, json=payload, headers=headers)
            
#             self.log(f"Response status code: {response.status_code}")
            
#             if response.status_code != 200:
#                 self.log(f"Error: API returned status code {response.status_code}")
#                 self.log(f"Response content: {response.text}")
#                 self.root.after(0, self.end_generation)
#                 return
            
#             # Parse response
#             try:
#                 creation_data = response.json()
#                 self.log(f"Creation started with ID: {creation_data.get('id')}")
                
#                 # Wait for creation to complete
#                 self.wait_for_creation(creation_data.get('id'))
                
#             except json.JSONDecodeError:
#                 self.log("Error: Could not parse JSON response")
#                 self.root.after(0, self.end_generation)
        
#         except Exception as e:
#             self.log(f"Error during generation: {str(e)}")
#             self.root.after(0, self.end_generation)
    
#     def wait_for_creation(self, creation_id, max_wait_time=300, check_interval=5):
#         """Wait for an image creation to complete"""
#         start_time = time.time()
        
#         while time.time() - start_time < max_wait_time:
#             self.log(f"Checking status of creation {creation_id}...")
            
#             # Check status
#             url = f"https://api.starryai.com/creations/{creation_id}"
#             headers = {
#                 "accept": "application/json",
#                 "X-API-Key": self.api_key
#             }
            
#             response = requests.get(url, headers=headers)
            
#             if response.status_code != 200:
#                 self.log(f"Error checking status: API returned status code {response.status_code}")
#                 self.log(f"Response: {response.text}")
#                 self.root.after(0, self.end_generation)
#                 return
            
#             try:
#                 status_data = response.json()
#                 status = status_data.get("status")
#                 self.log(f"Current status: {status}")
                
#                 if status == "completed":
#                     # Process completed images
#                     self.process_completed_images(status_data)
#                     return
#                 elif status == "failed":
#                     self.log("Creation failed")
#                     self.root.after(0, self.end_generation)
#                     return
                
#                 self.log(f"Waiting {check_interval} seconds before checking again...")
#                 time.sleep(check_interval)
                
#             except json.JSONDecodeError:
#                 self.log("Error: Could not parse JSON response")
#                 self.root.after(0, self.end_generation)
#                 return
        
#         self.log(f"Timed out after {max_wait_time} seconds")
#         self.root.after(0, self.end_generation)
    
#     def process_completed_images(self, completed_data):
#         """Process and display completed images"""
#         if "images" not in completed_data or not completed_data["images"]:
#             self.log("No images found in completed data")
#             self.root.after(0, self.end_generation)
#             return
        
#         images = completed_data["images"]
#         self.log(f"Found {len(images)} generated images")
        
#         # Store image URLs
#         self.generated_image_urls = [img["url"] for img in images if img.get("url")]
        
#         # Display images
#         self.root.after(0, lambda: self.display_images(self.generated_image_urls))
    
#     def display_images(self, image_urls):
#         """Display images in the UI"""
#         try:
#             # Calculate grid dimensions
#             num_images = len(image_urls)
#             cols = 2  # Fixed at 2 columns
#             rows = (num_images + cols - 1) // cols
            
#             # Configure grid
#             for i in range(cols):
#                 self.images_frame.columnconfigure(i, weight=1, minsize=400)
            
#             # Download and display each image
#             for i, url in enumerate(image_urls):
#                 # Calculate grid position
#                 row = i // cols
#                 col = i % cols
                
#                 # Create frame for this image
#                 img_frame = ttk.Frame(self.images_frame, padding=5, borderwidth=2, relief="ridge")
#                 img_frame.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
                
#                 # Make image frame expand to fill its cell
#                 img_frame.columnconfigure(0, weight=1)
#                 img_frame.rowconfigure(0, weight=1)
                
#                 # Add placeholder while loading
#                 placeholder_label = ttk.Label(img_frame, text="Loading image...", font=("Arial", 12))
#                 placeholder_label.grid(row=0, column=0, padx=5, pady=5)
                
#                 # Start a thread to download the image
#                 thread = threading.Thread(
#                     target=self.load_image_thread,
#                     args=(url, img_frame, placeholder_label, i)
#                 )
#                 thread.daemon = True
#                 thread.start()
            
#             # Update canvas scroll region
#             self.images_frame.update_idletasks()
#             self.images_canvas.configure(scrollregion=self.images_canvas.bbox("all"))
            
#         except Exception as e:
#             self.log(f"Error displaying images: {str(e)}")
        
#         finally:
#             # End generation process
#             self.end_generation()
    
#     def load_image_thread(self, url, frame, placeholder_label, index):
#         """Thread function to load an image from URL"""
#         try:
#             # Download the image
#             response = requests.get(url)
#             if response.status_code != 200:
#                 self.root.after(0, lambda: self.log(f"Error downloading image {index+1}: Status code {response.status_code}"))
#                 return
            
#             # Create PIL Image from bytes
#             img = Image.open(BytesIO(response.content))
            
#             # Calculate display size with fixed width but maintaining aspect ratio
#             display_width = 350  # Fixed width for display
#             display_height = int(img.height * (display_width / img.width))
            
#             # Resize for display (maintaining aspect ratio)
#             img_resized = img.resize((display_width, display_height), Image.Resampling.LANCZOS)
            
#             # Convert to PhotoImage
#             photo = ImageTk.PhotoImage(img_resized)
#             self.image_references.append(photo)  # Keep a reference
            
#             # Remove placeholder
#             self.root.after(0, lambda: placeholder_label.grid_forget())
            
#             # Create and display the image label with proper grid configuration
#             def display_image():
#                 image_label = ttk.Label(frame, image=photo)
#                 image_label.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
                
#                 # Add URL label
#                 url_text = f"Image {index+1}"
#                 url_label = ttk.Label(frame, text=url_text, cursor="hand2")
#                 url_label.bind("<Button-1>", lambda e, u=url: webbrowser.open(u))
#                 url_label.grid(row=1, column=0, padx=5, pady=(0, 5), sticky="w")
                
#                 # Add button frame for organizing buttons
#                 button_frame = ttk.Frame(frame)
#                 button_frame.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
                
#                 # Add save button
#                 save_button = ttk.Button(
#                     button_frame, 
#                     text="Save Image", 
#                     command=lambda u=url, i=index: self.save_image(u, i)
#                 )
#                 save_button.pack(side=tk.LEFT, padx=5)
                
#                 # Update canvas scroll region to ensure all content is visible
#                 self.images_frame.update_idletasks()
#                 self.images_canvas.configure(scrollregion=self.images_canvas.bbox("all"))
            
#             self.root.after(0, display_image)
            
#         except Exception as e:
#             self.root.after(0, lambda: self.log(f"Error loading image {index+1}: {str(e)}"))
    
#     def save_image(self, url, index):
#         """Save an image to disk"""
#         try:
#             # Ask user for save location
#             file_types = [('PNG Image', '*.png'), ('JPEG Image', '*.jpg')]
#             filename = filedialog.asksaveasfilename(
#                 defaultextension=".png",
#                 filetypes=file_types,
#                 title="Save Image As",
#                 initialfile=f"starryai_{int(time.time())}_{index+1}"
#             )
            
#             if not filename:  # User cancelled
#                 return
                
#             # Download the image
#             response = requests.get(url)
#             if response.status_code != 200:
#                 self.log(f"Error downloading image for saving: Status code {response.status_code}")
#                 return
            
#             # Save the image
#             with open(filename, "wb") as f:
#                 f.write(response.content)
                
#             self.log(f"Image saved to {filename}")
            
#         except Exception as e:
#             self.log(f"Error saving image: {str(e)}")
    
#     def end_generation(self):
#         """End the generation process, reset UI"""
#         self.generate_button.configure(state="normal")
#         self.progress.stop()
#         self.status_var.set("Ready")

# def main():
#     root = tk.Tk()
#     app = StarryAIGenerator(root)
#     root.mainloop()

# if __name__ == "__main__":
#     main()


















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