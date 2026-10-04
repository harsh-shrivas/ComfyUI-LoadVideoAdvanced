# ComfyUI-LoadVideoAdvanced

A high-performance, precision video loader and frame pre-processor node for ComfyUI.

Built for VFX artists, animators, and AI video pipelines who require fine-grained control over video frame ingestion. Eliminates memory bottlenecks by providing explicit frame start offsets, frame slice limits, aspect-ratio-aware dimensions, customizable crop padding, target playback FPS normalization, and comprehensive pipeline metadata pass-through.

---

## Features

* **Precision Frame Slicing:** Ingest exact frame ranges with dedicated `frame_start` and `frame_count` parameters to avoid loading entire high-resolution files into memory.
* **Custom Resolution & Padding:** Configure explicit `target_width` and `target_height` with integrated `crop_padding` to standardize footage before feeding latent encoders.
* **Target FPS Normalization:** Normalize incoming footage frame rates to a uniform `fps_target` for consistent temporal conditioning across animation workflows.
* **Optional Audio Ingestion:** Toggle audio extraction on or off to feed synchronized audio pipelines or mute unwanted tracks.
* **Rich Pipeline Metadata:** Simultaneously outputs the frame batch tensor, mask channel, audio dictionary, multi-line `video_info`, concise `video_meta_text`, and the sanitized `file_path` for downstream automation.

---

## Installation

1. Navigate to your ComfyUI custom nodes directory: `cd ComfyUI/custom_nodes`
2. Clone this repository: `git clone https://github.com/harsh-shrivas/ComfyUI-LoadVideoAdvanced.git`
3. Restart ComfyUI. (Zero external packages required).

---

## Usage

* **Category:** `Video Helpers`
* **Node Name:** `LoadVideoAdvanced`
* **Workflow:**
  1. Paste the absolute path to your video file into `video_path` (e.g., `Path\To\video.mov`).
  2. Set `frame_start` and `frame_count` to isolate the exact clip segment needed.
  3. Adjust `target_width`, `target_height`, and `fps_target` to match your project specifications.
  4. Route the `IMAGE` output to your VAE encode or conditioning nodes, `mask` to inpainting/control pipelines, and `video_meta_text` to logging or prompt nodes.

---

## Inputs & Outputs

| Parameter | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| **video_path** | `STRING` (Input) | `""` | Absolute path to the source video file |
| **frame_start** | `INT` (Input) | `0` | Starting frame index to begin ingestion |
| **frame_count** | `INT` (Input) | `856` | Maximum number of frames to load |
| **target_width** | `INT` (Input) | `480` | Target horizontal resolution |
| **target_height** | `INT` (Input) | `0` | Target vertical resolution (0 for auto/dynamic) |
| **crop_padding** | `INT` (Input) | `0` | Boundary crop padding in pixels |
| **fps_target** | `FLOAT` (Input) | `20.0` | Target playback frame rate |
| **extract_audio** | `BOOLEAN` (Input) | `True` | Whether to extract accompanying audio stream |
| **IMAGE** | `IMAGE` (Output) | — | Loaded video frames as an image batch tensor |
| **mask** | `MASK` (Output) | — | Alpha/transparency mask channel tensor |
| **audio** | `AUDIO` (Output) | — | Extracted audio stream dictionary |
| **video_info** | `STRING` (Output) | — | Multi-line technical summary (resolution, frames, FPS) |
| **video_meta_text** | `STRING` (Output) | — | Single-line metadata string for automated file naming |
| **file_path** | `STRING` (Output) | — | Sanitized absolute path of the loaded file |

---

## License

MIT License. Free to use, modify, and integrate into personal and studio pipelines.
