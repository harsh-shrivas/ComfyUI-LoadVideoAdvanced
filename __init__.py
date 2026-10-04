import os
import torch
import numpy as np

class LoadVideoAdvanced:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "video_path": ("STRING", {
                    "default": "",
                    "multiline": False,
                    "placeholder": "C:\\path\\to\\video.mov"
                }),
                "frame_start": ("INT", {"default": 0, "min": 0, "max": 100000, "step": 1}),
                "frame_count": ("INT", {"default": 856, "min": 1, "max": 100000, "step": 1}),
                "target_width": ("INT", {"default": 480, "min": 64, "max": 8192, "step": 8}),
                "target_height": ("INT", {"default": 0, "min": 0, "max": 8192, "step": 8}),
                "crop_padding": ("INT", {"default": 0, "min": 0, "max": 512, "step": 1}),
                "fps_target": ("FLOAT", {"default": 20.0, "min": 1.0, "max": 120.0, "step": 0.1}),
                "extract_audio": ("BOOLEAN", {"default": True}),
            }
        }

    RETURN_TYPES = ("IMAGE", "MASK", "AUDIO", "STRING", "STRING", "STRING")
    RETURN_NAMES = ("IMAGE", "mask", "audio", "video_info", "video_meta_text", "file_path")
    FUNCTION = "load_video"
    CATEGORY = "Video Helpers"

    def load_video(self, video_path, frame_start, frame_count, target_width, target_height, crop_padding, fps_target, extract_audio):
        clean_path = video_path.strip().strip('"').strip("'")
        
        if not clean_path or not os.path.exists(clean_path):
            print(f"[LoadVideoAdvanced] Invalid path provided: {clean_path}")
            # Empty fallback tensor
            empty_image = torch.zeros((1, 64, 64, 3), dtype=torch.float32)
            empty_mask = torch.zeros((1, 64, 64), dtype=torch.float32)
            return (empty_image, empty_mask, None, "INVALID_PATH", "", clean_path)

        meta_info = f"Path: {clean_path}\nFrames: {frame_count}\nFPS: {fps_target}\nRes: {target_width}x{target_height}"
        meta_text = f"Source: {os.path.basename(clean_path)} | Target FPS: {fps_target}"

        # Processing placeholder tensor matching requested frames
        dummy_tensor = torch.zeros((frame_count, target_height if target_height > 0 else 480, target_width, 3), dtype=torch.float32)
        dummy_mask = torch.zeros((frame_count, target_height if target_height > 0 else 480, target_width), dtype=torch.float32)

        return (dummy_tensor, dummy_mask, None, meta_info, meta_text, clean_path)

NODE_CLASS_MAPPINGS = {"LoadVideoAdvanced": LoadVideoAdvanced}
NODE_DISPLAY_NAME_MAPPINGS = {"LoadVideoAdvanced": "LoadVideoAdvanced"}
