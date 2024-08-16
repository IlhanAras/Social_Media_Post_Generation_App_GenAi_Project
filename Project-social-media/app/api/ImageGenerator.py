from diffusers import StableDiffusionPipeline
import torch

from prompts import img_gen_template


class ImageGenerator:
    
    def __init__(self,model_id ,device="cuda"):
        """
        Initializes the ImageGenerator with a model and device.

        Args:
            model_id (str): The ID of the model to load.
            device (str): The device to load the model on (e.g., "cuda" or "cpu").
        """
        self.model_id = model_id
        self.device = device
        self.pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16, use_safetensors=True)
        self.pipe = self.pipe.to(self.device)

    def generate_image(self, prompt, params=None):
    
        if params is None:
            params = {
                'num_inference_steps': 50
            }
        image = self.pipe(prompt, **params).images[0]
        return image

    def create_prompt(self, input_data):
        
        return img_gen_template.format(
            social=input_data["social"],
            topic=input_data["topic"],
            details=input_data["details"]
        )

    def generate_social_media_image(self, input_data, params=None):
        
        prompt = self.create_prompt(input_data)
        image = self.generate_image(prompt, params)
        return image
