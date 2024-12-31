Fine-tuning | How-to guides[Skip to main content](#mdc-main-content)[![](https://static.xx.fbcdn.net/rsrc.php/y9/r/tL_v571NdZ0.svg)](/)DocumentationTrust & SafetyCommunity[Try Llama](https://www.meta.ai/?utm_source=llama_meta_site&utm_medium=web&utm_content=Llama_nav&utm_campaign=July_moment)[Download models](/llama-downloads)
### Table Of ContentsFine-tuning

[Overview](/docs/overview)[Models](/docs/model-cards-and-prompt-formats)[Llama 3.3 (New)](/docs/model-cards-and-prompt-formats/llama3_3)[Llama 3.2](/docs/model-cards-and-prompt-formats/llama3_2)[Llama 3.1](/docs/model-cards-and-prompt-formats/llama3_1)[Llama Guard 3](/docs/model-cards-and-prompt-formats/llama-guard-3)[Prompt Guard](/docs/model-cards-and-prompt-formats/prompt-guard)[Other models](/docs/model-cards-and-prompt-formats/other-models)[Getting the Models](/docs/getting_the_models)[Meta](/docs/getting_the_models/meta)[Hugging Face](/docs/getting-the-models/hugging-face)[Kaggle](/docs/getting-the-models/kaggle)[1B/3B Partners](/docs/getting-the-models/1b3b-partners)[405B Partners](/docs/getting-the-models/405b-partners)[Running Llama](/docs/llama-everywhere)[Linux](/docs/llama-everywhere/running-meta-llama-on-linux/)[Windows](/docs/llama-everywhere/running-meta-llama-on-windows/)[Mac](/docs/llama-everywhere/running-meta-llama-on-mac/)[Cloud](/docs/llama-everywhere/running-meta-llama-in-the-cloud/)[How-To Guides](/docs/how-to-guides)[Fine-tuning](/docs/how-to-guides/fine-tuning)[Quantization](/docs/how-to-guides/quantization)[Prompting](/docs/how-to-guides/prompting)[Validation](/docs/how-to-guides/validation)[Vision Capabilities](/docs/how-to-guides/vision-capabilities/)[Responsible Use](/docs/how-to-guides/responsible-use-guide-resources/)[Integration Guides](/docs/integration-guides)[Code Llama](/docs/integration-guides/meta-code-llama)[LangChain](/docs/integration-guides/langchain)[Llamalndex](/docs/integration-guides/llamaindex)[Community Support](/docs/community-support-and-resources)[Resources](/docs/community-support-and-resources)

---

[Overview](/docs/overview)[Models](/docs/model-cards-and-prompt-formats)[Llama 3.3 (New)](/docs/model-cards-and-prompt-formats/llama3_3)[Llama 3.2](/docs/model-cards-and-prompt-formats/llama3_2)[Llama 3.1](/docs/model-cards-and-prompt-formats/llama3_1)[Llama Guard 3](/docs/model-cards-and-prompt-formats/llama-guard-3)[Prompt Guard](/docs/model-cards-and-prompt-formats/prompt-guard)[Other models](/docs/model-cards-and-prompt-formats/other-models)[Getting the Models](/docs/getting_the_models)[Meta](/docs/getting_the_models/meta)[Hugging Face](/docs/getting-the-models/hugging-face)[Kaggle](/docs/getting-the-models/kaggle)[1B/3B Partners](/docs/getting-the-models/1b3b-partners)[405B Partners](/docs/getting-the-models/405b-partners)[Running Llama](/docs/llama-everywhere)[Linux](/docs/llama-everywhere/running-meta-llama-on-linux/)[Windows](/docs/llama-everywhere/running-meta-llama-on-windows/)[Mac](/docs/llama-everywhere/running-meta-llama-on-mac/)[Cloud](/docs/llama-everywhere/running-meta-llama-in-the-cloud/)[How-To Guides](/docs/how-to-guides)[Fine-tuning](/docs/how-to-guides/fine-tuning)[Quantization](/docs/how-to-guides/quantization)[Prompting](/docs/how-to-guides/prompting)[Validation](/docs/how-to-guides/validation)[Vision Capabilities](/docs/how-to-guides/vision-capabilities/)[Responsible Use](/docs/how-to-guides/responsible-use-guide-resources/)[Integration Guides](/docs/integration-guides)[Code Llama](/docs/integration-guides/meta-code-llama)[LangChain](/docs/integration-guides/langchain)[Llamalndex](/docs/integration-guides/llamaindex)[Community Support](/docs/community-support-and-resources)[Resources](/docs/community-support-and-resources)How-to guides

Fine-tuning
===========

If you are looking to learn by writing code it's highly recommended to look into the [Getting to Know Llama 3](https://github.com/meta-llama/llama-recipes/blob/main/recipes/quickstart/Getting_to_know_Llama.ipynb) notebook. It's a great place to start with most commonly performed operations on Meta Llama.

Fine-tuning
-----------

Full parameter fine-tuning is a method that fine-tunes all the parameters of all the layers of the pre-trained model. In general, it can achieve the best performance but it is also the most resource-intensive and time consuming: it requires most GPU resources and takes the longest.

PEFT, or Parameter Efficient Fine Tuning, allows one to fine tune models with minimal resources and costs. There are two important PEFT methods: LoRA (Low Rank Adaptation) and QLoRA (Quantized LoRA), where pre-trained models are loaded to GPU as quantized 8-bit and 4-bit weights, respectively. It’s likely that you can fine-tune the Llama 2-13B model using LoRA or QLoRA fine-tuning with a single consumer GPU with 24GB of memory, and using QLoRA requires even less GPU memory and fine-tuning time than LoRA.

Typically, one should try LoRA, or if resources are extremely limited, QLoRA, first, and after the fine-tuning is done, evaluate the performance. Only consider full fine-tuning when the performance is not desirable.

Experiment tracking
-------------------

Experiment tracking is crucial when evaluating various fine-tuning methods like LoRA, and QLoRA. It ensures reproducibility, maintains a structured version history, allows for easy collaboration, and aids in identifying optimal training configurations. Especially with numerous iterations, hyperparameters, and model versions at play, tools like [Weights & Biases](https://wandb.ai/) (W&B) become indispensable. With its seamless integration into multiple frameworks, W&B provides a comprehensive dashboard to visualize metrics, compare runs, and manage model checkpoints. It's often as simple as adding a single argument to your training script to realize these benefits - we’ll show an example in the Hugging Face PEFT LoRA section.

Recipes PEFT LoRA
-----------------

The llama-recipes repo has details on different [fine-tuning](https://github.com/facebookresearch/llama-recipes/blob/main/docs/LLM_finetuning.md) (FT) alternatives supported by the provided sample scripts. In particular, it highlights the use of PEFT as the preferred FT method, as it reduces the hardware requirements and prevents catastrophic forgetting. For specific cases, full parameter FT can still be valid, and different strategies can be used to still prevent modifying the model too much. Additionally, FT can be done in [single gpu](https://github.com/facebookresearch/llama-recipes/blob/main/docs/single_gpu.md) or [multi-gpu](https://github.com/facebookresearch/llama-recipes/blob/main/docs/multi_gpu.md) with FSDP.

In order to run the recipes, follow the steps below:

1. Create a conda environment with pytorch and additional dependencies
2. Install the recipes as described [here](https://github.com/facebookresearch/llama-recipes#install-with-pip):
3. Download the desired model from hf, either using git-lfs or using the llama download script.
4. With everything configured, run the following command:

```
python -m llama_recipes.finetuning \ --use_peft --peft_method lora --quantization \ --model_name ../llama/models_hf/7B \ --output_dir ../llama/models_ft/7B-peft \ --batch_size_training 2 --gradient_accumulation_steps 2
```

torchtune ([link](https://github.com/pytorch/torchtune))
--------------------------------------------------------

torchtune is a PyTorch-native library that can be used to fine-tune the Meta Llama family of models including Meta Llama 3. It supports the [end-to-end fine-tuning lifecycle](https://pytorch.org/torchtune/stable/tutorials/e2e_flow.html) including:

* Downloading model checkpoints and datasets
* Training recipes for [fine-tuning Llama 3](https://pytorch.org/torchtune/stable/tutorials/llama3.html) using full fine-tuning, LoRA, and QLoRA
* Support for single-GPU fine-tuning capable of running on consumer-grade GPUs with 24GB of VRAM
* Scaling fine-tuning to multiple GPUs using PyTorch FSDP
* Log metrics and model checkpoints during training using Weights & Biases
* Evaluation of fine-tuned models using EleutherAI’s LM Evaluation Harness
* Post-training quantization of fine-tuned models via TorchAO
* Interoperability with inference engines including ExecuTorch

To [install torchtune](https://pytorch.org/torchtune/stable/install.html) simply run the pip install command
```
pip install torchtune
```
Follow the instructions on the Hugging Face [meta-llama](https://huggingface.co/meta-llama/Meta-Llama-3-8B) repository to ensure you have access to the Llama 3 model weights. Once you have confirmed access, you can run the following command to download the weights to your local machine. This will also download the tokenizer model and a responsible use guide.
```
tune download meta-llama/Meta-Llama-3-8B \ --output-dir <checkpoint_dir> \ --hf-token <ACCESS TOKEN>
```
Set your environment variable HF\_TOKEN or pass in --hf-token to the command in order to validate your access. You can find your token at <https://huggingface.co/settings/tokens>

The basic command for a single-device LoRA fine-tune of Llama 3 is

```
tune run lora_finetune_single_device --config llama3/8B_lora_single_device
```

torchtune contains built-in recipes for:

* Full fine-tuning on [single device](https://github.com/pytorch/torchtune/blob/main/recipes/full_finetune_single_device.py) and on [multiple devices with FSDP](https://github.com/pytorch/torchtune/blob/main/recipes/full_finetune_distributed.py)
* LoRA finetuning on [single device](https://github.com/pytorch/torchtune/blob/main/recipes/lora_finetune_single_device.py) and on [multiple devices with FSDP](https://github.com/pytorch/torchtune/blob/main/recipes/lora_finetune_distributed.py).
* QLoRA finetuning on [single device](https://github.com/pytorch/torchtune/blob/main/recipes/lora_finetune_single_device.py), with a QLoRA specific [configuration](https://github.com/pytorch/torchtune/blob/main/recipes/configs/llama3/8B_qlora_single_device.yaml)

You can find more information on fine-tuning Meta Llama models by reading the torchtune [Getting Started](https://github.com/pytorch/torchtune?tab=readme-ov-file#get-started) guide.

Hugging Face PEFT LoRA ([link](https://github.com/huggingface/peft))
--------------------------------------------------------------------

Using Low Rank Adaption (LoRA) , Meta Llama is loaded to the GPU memory as quantized 8-bit weights.

Using the Hugging Face Fine-tuning with PEFT LoRA ([link](https://huggingface.co/blog/llama2#fine-tuning-with-peft)) is super easy - an example fine-tuning run on Meta Llama 2 7b using the OpenAssistant data set can be done in three simple steps:
```
pip install trl git clone https://github.com/huggingface/trl python trl/examples/scripts/sft.py \ --model_name meta-llama/Llama-2-7b-hf \ --dataset_name timdettmers/openassistant-guanaco \ --load_in_4bit \ --use_peft \ --batch_size 4 \ --gradient_accumulation_steps 2 \ --log_with wandb
```

This takes about 16 hours on a single GPU and uses less than 10GB GPU memory; changing batch size to 8/16/32 will use over 11/16/25 GB GPU memory. After the fine-tuning completes, you’ll see in a new directory named “output” at least adapter\_config.json and adapter\_model.bin - run the script below to infer with the base model and the new model, generated by merging the base model with the fined-tuned one:

```
import torch from transformers import ( AutoModelForCausalLM, AutoTokenizer, pipeline, ) from peft import LoraConfig, PeftModel from trl import SFTTrainer model_name="meta-llama/Llama-2-7b-chat-hf" new_model="output" device_map={"": 0} base_model=AutoModelForCausalLM.from_pretrained( model_name, low_cpu_mem_usage=True, return_dict=True, torch_dtype=torch.float16, device_map=device_map, ) model=PeftModel.from_pretrained(base_model, new_model) model=model.merge_and_unload() tokenizer=AutoTokenizer.from_pretrained(model_name, trust_remote_code=True) tokenizer.pad_token=tokenizer.eos_token tokenizer.padding_side="right" prompt="Who wrote the book Innovator's Dilemma?" pipe=pipeline(task="text-generation", model=base_model, tokenizer=tokenizer, max_length=200) result=pipe(f"<s>[INST] {prompt} [/INST]") print(result[0]['generated_text']) pipe=pipeline(task="text-generation", model=model, tokenizer=tokenizer, max_length=200) result=pipe(f"<s>[INST] {prompt} [/INST]") print(result[0]['generated_text'])
```

QLoRA Fine TuningQLoRA (Q for quantized) is more memory efficient than LoRA. In QLoRA, the pretrained model is loaded to the GPU as quantized 4-bit weights. Fine-tuning using QLoRA is also very easy to run - an example of fine-tuning Llama 2-7b with the OpenAssistant can be done in four quick steps:

```
git clone https://github.com/artidoro/qlora cd qlora pip install -U -r requirements.txt ./scripts/finetune_llama2_guanaco_7b.sh
```

It takes about 6.5 hours to run on a single GPU, using 11GB memory of the GPU. After the fine-tuning completes and the output\_dir specified in ./scripts/finetune\_llama2\_guanaco\_7b.sh will have checkoutpoint-xxx subfolders, holding the fine-tuned adapter model files. To run inference, use the script below:

```
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, pipeline from peft import LoraConfig, PeftModel import torch model_id="meta-llama/Llama-2-7b-hf" new_model="output/llama-2-guanaco-7b/checkpoint-1875/adapter_model" # change if needed quantization_config=BitsAndBytesConfig( load_in_4bit=True, bnb_4bit_compute_dtype=torch.bfloat16, bnb_4bit_use_double_quant=True, bnb_4bit_quant_type='nf4' ) model=AutoModelForCausalLM.from_pretrained( model_id, low_cpu_mem_usage=True, load_in_4bit=True, quantization_config=quantization_config, torch_dtype=torch.float16, device_map='auto' ) model=PeftModel.from_pretrained(model, new_model) tokenizer=AutoTokenizer.from_pretrained(model_id) prompt="Who wrote the book innovator's dilemma?" pipe=pipeline(task="text-generation", model=model, tokenizer=tokenizer, max_length=200) result=pipe(f"<s>[INST] {prompt} [/INST]") print(result[0]['generated_text'])
```
[Axolotl](https://github.com/OpenAccess-AI-Collective/axolotl) is another open source library you can use to streamline the fine-tuning of Llama 2. A good example of using Axolotl to fine-tune Meta Llama with four notebooks covering the whole fine-tuning process (generate the dataset, fine-tune the model using LoRA, evaluate and benchmark) is [here](https://github.com/OpenPipe/OpenPipe/tree/main/examples/classify-recipes).

QLoRA Fine Tuning
-----------------

Note: This has been tested on Meta Llama 2 models only.

QLoRA (Q for quantized) is more memory efficient than LoRA. In QLoRA, the pretrained model is loaded to the GPU as quantized 4-bit weights. Fine-tuning using QLoRA is also very easy to run - an example of fine-tuning Llama 2-7b with the OpenAssistant can be done in four quick steps:

```
git clone https://github.com/artidoro/qlora cd qlora pip install -U -r requirements.txt ./scripts/finetune_llama2_guanaco_7b.sh
```

It takes about 6.5 hours to run on a single GPU, using 11GB memory of the GPU. After the fine-tuning completes and the output\_dir specified in ./scripts/finetune\_llama2\_guanaco\_7b.sh will have checkoutpoint-xxx subfolders, holding the fine-tuned adapter model files. To run inference, use the script below:

```
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, pipeline from peft import LoraConfig, PeftModel import torch model_id="meta-llama/Llama-2-7b-hf" new_model="output/llama-2-guanaco-7b/checkpoint-1875/adapter_model" # change if needed quantization_config=BitsAndBytesConfig( load_in_4bit=True, bnb_4bit_compute_dtype=torch.bfloat16, bnb_4bit_use_double_quant=True, bnb_4bit_quant_type='nf4' ) model=AutoModelForCausalLM.from_pretrained( model_id, low_cpu_mem_usage=True, load_in_4bit=True, quantization_config=quantization_config, torch_dtype=torch.float16, device_map='auto' ) model=PeftModel.from_pretrained(model, new_model) tokenizer=AutoTokenizer.from_pretrained(model_id) prompt="Who wrote the book innovator's dilemma?" pipe=pipeline(task="text-generation", model=model, tokenizer=tokenizer, max_length=200) result=pipe(f"<s>[INST] {prompt} [/INST]") print(result[0]['generated_text'])
```

Note: This has been tested on Meta Llama 2 models only.

[Axolotl](https://github.com/OpenAccess-AI-Collective/axolotl) is another open source library you can use to streamline the fine-tuning of Llama 2. A good example of using Axolotl to fine-tune Meta Llama with four notebooks covering the whole fine-tuning process (generate the dataset, fine-tune the model using LoRA, evaluate and benchmark) is [here](https://github.com/OpenPipe/OpenPipe/tree/main/examples/classify-recipes).Was this page helpful?YesNoOn this page[Fine-tuning](#fine-tuning)[Fine-tuning](#fine-tuning)[Experiment tracking](#experiment-tracking)[Recipes PEFT LoRA](#recipes-peft-lora)[torchtune (link)](#torchtune-(link))[Hugging Face PEFT LoRA (link)](#hugging-face-peft-lora-(link))[QLoRA Fine Tuning](#qlora-fine-tuning)

---

![](https://static.xx.fbcdn.net/rsrc.php/y9/r/tL_v571NdZ0.svg)[![](https://scontent.fblr24-1.fna.fbcdn.net/v/t39.2365-6/301846186_1133977354136753_4449523448606696437_n.svg?_nc_cat=104&ccb=1-7&_nc_sid=aa6a2f&_nc_ohc=N6gSxsE-TDoQ7kNvgG6dGUd&_nc_zt=14&_nc_ht=scontent.fblr24-1.fna&_nc_gid=Axymi87sCwomNRbB8juGVA0&oh=00_AYDl9essjNhjF7kMQOXptcd5rNB2HcYCqodEf4BxGDcuag&oe=6776E8C3)](https://www.facebook.com/AIatMeta/)[![](https://scontent.fblr24-1.fna.fbcdn.net/v/t39.2365-6/467665288_1952116298626027_4990190601706024947_n.svg?_nc_cat=106&ccb=1-7&_nc_sid=aa6a2f&_nc_ohc=Wys8YKexG3UQ7kNvgFVMD_6&_nc_zt=14&_nc_ht=scontent.fblr24-1.fna&_nc_gid=Axymi87sCwomNRbB8juGVA0&oh=00_AYDNhC7qg_Bfc5Y0k7PdChY57FTfHI8fvB7hWizyyLsBjg&oe=67770F6A)](https://twitter.com/aiatmeta/)[![](https://scontent.fblr24-3.fna.fbcdn.net/v/t39.2365-6/301448763_775186710293873_8271592194986836260_n.svg?_nc_cat=102&ccb=1-7&_nc_sid=aa6a2f&_nc_ohc=iUAm50JOFAEQ7kNvgHjW4nD&_nc_zt=14&_nc_ht=scontent.fblr24-3.fna&_nc_gid=Axymi87sCwomNRbB8juGVA0&oh=00_AYB_45fSGuNJmsq326m963AayxuoiC_V5W-xHw8WQ2kmWA&oe=677711E7)](https://www.youtube.com/@aiatmeta)[![](https://scontent.fblr24-1.fna.fbcdn.net/v/t39.2365-6/467689750_1684384502343829_7561568713040200172_n.svg?_nc_cat=103&ccb=1-7&_nc_sid=aa6a2f&_nc_ohc=z9AsmhTzTRUQ7kNvgFKTTDC&_nc_zt=14&_nc_ht=scontent.fblr24-1.fna&_nc_gid=Axymi87sCwomNRbB8juGVA0&oh=00_AYCji62iah_BCxrIQaPljCuuFCluGQseyBkbCPRLBdvClQ&oe=677700BE)](https://www.linkedin.com/showcase/aiatmeta)Documentation[Overview](/docs/overview/)[Models](/docs/model-cards-and-prompt-formats) [Getting the Models](/docs/getting_the_models) [Running Llama](/docs/llama-everywhere) [How-To Guides](/docs/how-to-guides) [Integration Guides](/docs/integration-guides) [Community Support](/docs/community-support-and-resources) 

---

Community[Community Stories](/community-stories/)[Open Innovation AI Research Community](/open-innovation-ai-research-community/)[Llama Impact Grants](/llama-impact-grants/)

---

Resources[AI at Meta Blog](https://ai.meta.com/blog/)[Meta Newsroom](https://about.fb.com/news/)[FAQ](/faq)[Privacy Policy](https://www.facebook.com/privacy/policy/)[Terms](https://www.facebook.com/policies_center/)[Cookies](https://www.facebook.com/privacy/policies/cookies/?entry_point=cookie_policy_redirect&entry=0)

---

Trust & Safety[Overview](/trust-and-safety/)[Responsible Use Guide](/responsible-use-guide/)

---

Documentation[Overview](/docs/overview/)[Models](/docs/model-cards-and-prompt-formats) [Getting the Models](/docs/getting_the_models) [Running Llama](/docs/llama-everywhere) [How-To Guides](/docs/how-to-guides) [Integration Guides](/docs/integration-guides) [Community Support](/docs/community-support-and-resources) Community[Community Stories](/community-stories/)[Open Innovation AI Research Community](/open-innovation-ai-research-community/)[Llama Impact Grants](/llama-impact-grants/)Resources[AI at Meta Blog](https://ai.meta.com/blog/)[Meta Newsroom](https://about.fb.com/news/)[FAQ](/faq)[Privacy Policy](https://www.facebook.com/privacy/policy/)[Terms](https://www.facebook.com/policies_center/)[Cookies](https://www.facebook.com/privacy/policies/cookies/?entry_point=cookie_policy_redirect&entry=0)Trust & Safety[Overview](/trust-and-safety/)[Responsible Use Guide](/responsible-use-guide/)Documentation[Overview](/docs/overview/)[Models](/docs/model-cards-and-prompt-formats) [Getting the Models](/docs/getting_the_models) [Running Llama](/docs/llama-everywhere) [How-To Guides](/docs/how-to-guides) [Integration Guides](/docs/integration-guides) [Community Support](/docs/community-support-and-resources) Community[Community Stories](/community-stories/)[Open Innovation AI Research Community](/open-innovation-ai-research-community/)[Llama Impact Grants](/llama-impact-grants/)Resources[AI at Meta Blog](https://ai.meta.com/blog/)[Meta Newsroom](https://about.fb.com/news/)[FAQ](/faq)[Privacy Policy](https://www.facebook.com/privacy/policy/)[Terms](https://www.facebook.com/policies_center/)[Cookies](https://www.facebook.com/privacy/policies/cookies/?entry_point=cookie_policy_redirect&entry=0)Trust & Safety[Overview](/trust-and-safety/)[Responsible Use Guide](/responsible-use-guide/)Documentation[Overview](/docs/overview/)[Models](/docs/model-cards-and-prompt-formats) [Getting the Models](/docs/getting_the_models) [Running Llama](/docs/llama-everywhere) [How-To Guides](/docs/how-to-guides) [Integration Guides](/docs/integration-guides) [Community Support](/docs/community-support-and-resources) Community[Community Stories](/community-stories/)[Open Innovation AI Research Community](/open-innovation-ai-research-community/)[Llama Impact Grants](/llama-impact-grants/)Resources[AI at Meta Blog](https://ai.meta.com/blog/)[Meta Newsroom](https://about.fb.com/news/)[FAQ](/faq)[Privacy Policy](https://www.facebook.com/privacy/policy/)[Terms](https://www.facebook.com/policies_center/)[Cookies](https://www.facebook.com/privacy/policies/cookies/?entry_point=cookie_policy_redirect&entry=0)Trust & Safety[Overview](/trust-and-safety/)[Responsible Use Guide](/responsible-use-guide/)