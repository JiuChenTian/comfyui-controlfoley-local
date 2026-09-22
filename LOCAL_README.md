# ControlFoley 纯本地版

本版本保留原来的四个 ComfyUI 节点及其工作流输入输出。

默认模型目录：`C:\software\NovalAI\Comfy-Desktop\ComfyUI\ComfyUI\models\controlfoley`。
如需迁移，可设置环境变量 `CONTROLFOLEY_MODEL_DIR` 为新的完整模型目录。

## 本地加载

- CLIP：读取 `ext_weights/clip/open_clip_config.json` 与 `open_clip_pytorch_model.bin`。
- BigVGAN：读取 `ext_weights/bigvgan_v2/config.json` 与 `bigvgan_generator.pt`。
- MusicGen：读取 `ext_weights/musicgen/state_dict.bin` 与 `compression_state_dict.bin`。
- RoBERTa、T5、MERT：分别读取 `ext_weights/roberta-base`、`ext_weights/t5-base`、`ext_weights/MERT-v1-95M`。
- 主模型：`weights/controlfoley.pth`；VAE、CLAP、Synchformer、CAV-MAE：原来的 `ext_weights` 权重文件。

CLIP、BigVGAN、AudioCraft、Synchformer 的远程下载分支已移除；Transformers 加载均使用本地路径和 `local_files_only=True`。缺失文件会报出本地路径，不会自动下载。未使用全局网络拦截或修改其他插件的 Hugging Face 设置。

CLAP 所需推理源码位于 `lib/local_clap`，来源为本机 LAION CLAP 1.1.7，保留 CC0 许可证。此副本不导入原包的训练数据模块，避免其启动时加载额外 BERT/BART 模型。

原源码未发现独立的账号登录或授权校验；原先联网主要来自模型仓库查询和自动下载。

## 使用

将整个 `comfyui-controlfoley` 文件夹放入 ComfyUI 的 `custom_nodes`，重启 ComfyUI。不要同时加载原版和本地版。
运行 `check_local_models.py` 可检查所需文件。依赖使用现有 ComfyUI Python 环境；本插件不会自动安装依赖。

## 验证

在测试进程中拦截网络连接和域名解析，验证节点导入、整套特征模型加载、T5/MERT/CLAP 推理，并完成 2 秒、5 步的文本转音频测试。输出为 44100 Hz 单声道，未发生网络请求。
测试音频用于验证功能可运行，不代表正式生成的音质；正式使用可沿用原默认采样步数。
