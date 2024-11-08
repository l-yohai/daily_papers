# Daily Papers

## Project Description

This project aims to automatically translate and summarize [Huggingface's daily papers](https://huggingface.co/papers) into Korean using GPT-4o.

Thanks to [@AK391](https://github.com/AK391) for great work.

## Daily Papers (2024-11-08)

### [Both Text and Images Leaked! A Systematic Analysis of Multimodal LLM Data Contamination](https://arxiv.org/abs/2411.03823)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.03823.png)

Vote: 38

Authors: Benyou Wang, Lichao Sun, Shunian Chen, Dingjie Song, Sicheng Lai

- ***What's New***: 이 연구에서는 멀티모달 대규모 언어 모델(Multimodal Large Language Models; MLLMs)의 데이터 오염 문제를 체계적으로 분석하고, MLLMs에서 발생할 수 있는 데이터 누출의 단계를 탐색합니다. 특히, 최초로 멀티모달 데이터 오염 탐지 프레임워크인 MM-Detect를 소개하여 다양한 멀티모달 벤치마크에서 데이터 누출이 모델 성능에 미치는 영향을 정량적으로 평가합니다.
- ***Technical Details***: MM-Detect 프레임워크는 두 가지 주된 검출 방법인 옵션 순서 민감도 테스트(Option Order Sensitivity Test)와 슬럿 추측(Slot Guessing for Perturbation Caption)을 사용합니다. 이는 각각 다지선다형 질문과 이미지 캡션 작업에서의 오염을 평가하도록 설계되었습니다. 또한, 프레임워크는 사전훈련(pre-training)과 미세조정(fine-tuning) 단계에서의 오염 가능성을 구분하여 분석합니다.
- ***Performance Highlights***: 실험 결과, 오픈소스 및 독점 MLLMs 모두 다양한 모델에서 오염도가 다르게 나타났으며, 특히 벤치마크 데이터 셋의 누출은 테스트 세트에서 모델 성능을 크게 향상시킬 수 있음이 밝혀졌습니다. 이는 MLLMs가 훈련된 데이터로부터 불공정한 이점을 얻을 수 있음을 시사하며, 혼합 모달리티 훈련 (cross-modal alignment training)에서 추가적인 오염이 발생할 수 있음을 보여줍니다.

### [RetrieveGPT: Merging Prompts and Mathematical Models for Enhanced Code-Mixed Information Retrieval](https://arxiv.org/abs/2411.04752)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.04752.png)

Vote: 5

Authors: Aniket Deroy, Subhankar Maity

- ***What's New***: RetrieveGPT는 코드혼합(Code-Mixed) 데이터에서 정보를 효과적으로 추출하기 위한 새로운 접근 방식을 제안합니다. GPT-3.5 Turbo 모델과 수학적 모델을 결합하여 로마자 변환된 벵골어와 영어로 구성된 디지털 대화에서 관련 정보를 식별하는 방법을 개발하였습니다.
- ***Technical Details***: 이 연구는 Facebook에서 수집된 코드혼합 대화 데이터를 기반으로 하며, Query Relevance Files (QRels)를 사용해 쿼리의 관련성을 평가합니다. GPT-3.5 Turbo와 함께 프롬프트(prompt) 설계와 문서의 순차적 특성을 활용한 수학적 모델을 통합하여 관련 문서를 감지합니다. 이 과정은 입력 쿼리와 문서 간의 의미적 유사도를 평가하도록 최적화된 프롬프트의 사용을 포함합니다.
- ***Performance Highlights***: 실험에서는 다양한 평가 메트릭(MAP Score, ndcg Score, p@5 Score, p@10 Score)을 사용하여 성능을 비교하였으며, 텍스트자이탄스 팀의 다섯 번째 제출에서는 MAP Score가 0.703734로, ndcg Score가 0.799196로 다른 결과들보다 약간 향상되었습니다. 이는 각 쿼리에 대해 보다 관련성 높은 결과를 제공함을 나타냅니다.

### [SALSA: Soup-based Alignment Learning for Stronger Adaptation in RLHF](https://arxiv.org/abs/2411.01798)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.01798.png)

Vote: 7

Authors: Moin Nabi, Maxwell Horton, Keivan Alizadeh, Dong Yin, Mehrdad Farajtabar, Hamid Kazemi, Iman Mirzadeh, Atoosa Chegini

- ***What's New***: SALSA는 인간 피드백을 통한 강화 학습(RLHF)의 제약을 극복하기 위해 설계된 새로운 접근법으로, 모델 수프(모델 간의 가중치 평균화)를 참조 모델로 사용하여 보다 유연하고 탐색 범위를 넓히는 데 기여합니다.
- ***Technical Details***: SALSA는 모델 수프를 RLHF 프레임워크의 참조 모델로 통합하여, 독립적으로 감독된 Fine-Tuning(SFT) 모델 두 개의 가중치를 공간 평균화하여 생성합니다. 이 방법은 Kullback-Leibler(KL) 발산에서 더 큰 편차를 허용하며, 안정성을 포기하지 않고 해결 공간의 유망한 영역을 탐색할 수 있게 해줍니다.
- ***Performance Highlights***: SALSA는 다양한 벤치마크(MT-Bench, Arena-Hard, UltraFeedback)에서 PPO를 일관되게 능가하며, Llama2-7B, Mistral-7B, Gemma-2B 모델에서의 실험을 통해 탐색 심화를 통해 우수한 정렬 결과를 달성했습니다. SALSA의 수프 기반 접근은 향상된 보상, 모델의 견고함 및 분포 외 일반화를 입증합니다.

### [Correlation of Object Detection Performance with Visual Saliency and Depth Estimation](https://arxiv.org/abs/2411.02844)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.02844.png)

Vote: 3

Authors: Dylan Seychell, Matthias Bartolo

- ***What's New***: 이 논문은 객체 검출(Object Detection)의 정확도와 두 가지 중요한 시각적 작업인 깊이 예측(Depth Prediction) 및 시각 중요도(Visual Saliency) 예측 사이의 상관 관계를 조사합니다. 연구 결과, 시각 중요도가 깊이 예측보다 더 강한 상관 관계를 보이며, 객체의 크기별로 상관 관계가 다르게 나타난다는 사실을 발견했습니다.
- ***Technical Details***: 본 연구에서는 COCO와 Pascal VOC 데이터셋을 사용하여 깊이 예측 모델(Depth Anything, DPT-Large)과 시각 중요도 예측 모델(DeepGaze IIE, Itti’s Model)의 성능을 평가합니다. 각 이미지에 대한 예측 값과 실제 값의 피어슨 상관 계수(Pearson Correlation)를 측정하여, 각 객체 카테고리에 대한 평균 상관 계수(mAρ)를 계산했습니다.
- ***Performance Highlights***: Pascal VOC 데이터셋에서 시각 중요도 모델 DeepGaze IIE는 최대 mAρ 0.459를 기록하며 깊이 예측 모델보다 높은 정확도를 보여주었습니다. 반면, COCO 데이터셋에서는 복잡한 시각적 맥락 때문에 상대적으로 낮은 성능을 보였습니다. 이는 시각 중요도가 주어진 복잡한 시각적 맥락에서 객체 검출 정확도에 더 큰 영향을 미친다는 것을 시사합니다.

### [BitNet a4.8: 4-bit Activations for 1-bit LLMs](https://arxiv.org/abs/2411.04965)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.04965.png)

Vote: 29

Authors: Furu Wei, Shuming Ma, Hongyu Wang

- ***What's New***: BitNet a4.8은 1-bit 대형 언어 모델(LLMs)에서 4-bit 활성화(Activations)를 가능하게 하는 혁신적인 하이브리드 양자화(Quantization)와 희소화(Sparsification) 전략을 소개했습니다. 이를 통해 기존 모델인 BitNet b1.58과 동일한 훈련 비용으로 비슷한 성능을 내는 동시에 추론(Inference) 효율성을 크게 향상시켰습니다.
- ***Technical Details***: BitNet a4.8은 주의(attention) 및 전방 전파 네트워크(FFN)의 입력에 4-bit 양자화를 적용하고, 중간 상태는 8-bit로 희소화하여 높은 양자화 오류를 줄입니다. 본 모델은 W1.58A8에서 W1.58A4로 진행하며 1단계에서 8-bit 활성화와 ReLU2GLU 구조로 훈련하고, 2단계에서는 하이브리드 양자화와 희소화를 수행합니다. 그레이디언트 근사를 위해 STE(straight-through estimator)와 혼합 정밀도 훈련을 사용합니다.
- ***Performance Highlights***: BitNet a4.8은 FP16 LLaMA LLM과 비교했을 때 평균 정확도에서 거의 손실 없이 고급 입력을 보여주었으며, KL 배치를 통해 메모리 사용과 추론 시간을 크게 줄이는 데 성공했습니다. 특히, 7B 모델 크기에서 구체적인 희소화 전략을 통해 전체 희소도를 44.5%로 이뤘으며, 활성화된 파라미터는 55%에 불과하여 비활성화 파라미터의 중복적인 계산을 효과적으로 제거하였습니다.

### [Sparsing Law: Towards Large Language Models with Greater Activation Sparsity](https://arxiv.org/abs/2411.02335)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.02335.png)

Vote: 9

Authors: Xu Han, Maosong Sun, Yingfa Chen, Chenyang Song, Chaojun Xiao, Yuqi Luo, Zhiyuan Liu

- ***What's New***: 이 논문에서는 LLMs(Large Language Models)에서 활성화 희소성(Activation Sparsity)을 높이는 'Sparsing Law'를 제안합니다. 최신 활성화 희소성 메트릭인 PPL-p% 희소성을 사용하여 코드의 효율성 및 모델 해석성을 개선할 수 있으며, 활성화 희소성이 모델 성능과 어떻게 연관되는지에 대한 포괄적인 연구를 제공합니다.
- ***Technical Details***: 활성화 희소성은 뉴런 출력에서 기여도가 낮은 요소가 많이 존재하는 현상으로, 이는 계산 가속화 및 모델 해석성에 유리합니다. 이 논문은 디코더-온리(Decoder-Only) Transformer에 기반한 LLMs에서 다양한 활성화 함수(ReLU, SiLU)와 너비-깊이 비율 등 여러 요인들이 활성화 희소성에 어떻게 영향을 미치는지를 정량적으로 분석합니다. 활성화 희소성을 정확하고 성능 인식적으로 평가하는 PPL-p% 희소성을 제안하였습니다.
- ***Performance Highlights***: ReLU 활성화가 SiLU 활성화보다 높은 희소성을 달성하며, 훈련 데이터 양이 증가할수록 ReLU 활성화 모델은 로그 스페이스 거듭제곱 법칙에 따라 희소성이 증가하는 반면, SiLU는 일반 거듭제곱 법칙에 따라 감소합니다. 희소성은 너비-깊이 비율과 비례적으로 증가하며, 특정 매개 변수 스케일에서는 활성화 패턴이 파라미터 규모와 약하게 연관된다는 것을 발견했습니다.

### [Diff-2-in-1: Bridging Generation and Dense Perception with Diffusion Models](https://arxiv.org/abs/2411.05005)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.05005.png)

Vote: 2

Authors: Yu-Xiong Wang, Shuhong Zheng, Martial Hebert, Zhipeng Bao, Ruoyu Zhao

- ***What's New***: Diff-2-in-1은 생성과 밀집 시각 인식(dense perception)을 하나의 통합된 확산 모델(diffusion model)로 연결하는 새로운 프레임워크입니다. 이 프레임워크는 생성적 학습과 판별적 학습을 동시에 활용하여 다중 모달 데이터 생성과 효과적인 시각 예측을 가능하게 합니다.
- ***Technical Details***: Diff-2-in-1은 두 가지의 매개변수 세트를 사용하는 자기 향상(self-improving) 학습 메커니즘을 도입하였습니다. 이 메커니즘은 생성 과정에서 추가적인 다중 모달 데이터를 만들어내고, 이러한 데이터와 원본 데이터를 모두 활용하여 판별적 시각 인식 작업을 학습합니다. 또한, 생성된 데이터는 시간 단계 T에서의 확산-노이즈 제거(diffusion-denoising) 과정을 통해 더 높은 품질의 데이터를 점진적으로 생성하게 됩니다.
- ***Performance Highlights***: Diff-2-in-1은 다양한 판별 백본과 높은 품질의 다중 모달 데이터 생성에서 일관된 성능 향상을 보여줍니다. 특히, 사용자 정의 신경망을 거의 사용하지 않고도 최첨단의 성능을 보이며, 데이터의 효율성을 증대시키고, 다수의 시각 예측 작업에서의 성능을 대폭 개선하는 것을 입증하였습니다.

### ["Give Me BF16 or Give Me Death"? Accuracy-Performance Trade-Offs in LLM Quantization](https://arxiv.org/abs/2411.02355)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.02355.png)

Vote: 44

Authors: Eldar Kurtic, Mark Kurtz, Dan Alistarh, Shubhra Pandit, Alexandre Marques

- ***What's New***: 이 논문은 다양한 양자화 형식(FP8, INT8, INT4)에 따른 대형 언어 모델(LLM)의 성능 및 정확도 절충점을 체계적으로 탐구합니다. 특히, Llama-3.1 모델 전체에서 양자화된 모델과 압축되지 않은 모델 사이의 텍스트 차이를 평가하며, 최신 정확도 회복 결과를 달성하기 위한 몇 가지 양자화 개선점을 제시합니다.
- ***Technical Details***: 양자화를 위해 FP8, INT8, INT4 정수 양자화 형식(W8A8, W4A16)을 평가하였으며, NVIDIA의 다양한 GPU 아키텍처에서 vLLM 프레임워크를 사용하여 성능 분석을 수행했습니다. 주요 결과는 FP8이 모든 모델 크기에서 거의 손실 없이 작동하고, 잘 조정된 INT8이 낮은 정확도 저하(1-3%)를 유발하며, INT4 무게 양자화가 INT8만큼 경쟁력이 있음을 보여줍니다.
- ***Performance Highlights***: W4A16은 동기식 배치에서 뛰어난 비용 효율성을 제공하며, 중간 크기 GPU에서 비동기식 배치에 더 적합합니다. 한편, W8A8 형식은 고급 GPU에서의 비동기식 '연속 배치' 배포에 뛰어난 성능을 발휘합니다. 이는 LLM의 양자화된 해석 배치를 효율적으로 배치하기 위한 실질적인 지침을 제공합니다.

### [Hunyuan-Large: An Open-Source MoE Model with 52 Billion Activated Parameters by Tencent](https://arxiv.org/abs/2411.02265)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.02265.png)

Vote: 21

Authors: Shuang Chen, Jianglu Hu, Ruibin Chen, Yong Yang, Jie Jiang, Zhen Yang, Xuebin Hou, Xuemeng Huang, Jianfeng Yan, Jie Liu, Bin Hu, Jiawei Song, Zhenxiang Yan, Jinbao Xue, Winston Hu, Kai Zhang, Weiwen Jia, Yuhong Liu, Zhiyuan Xiong, Han Liu, Kai Liu, Chenchen Zhang, Kan Wu, Hao Fei, Hai Wang, Mengyuan Huang, Yangyu Tao, Di Wang, Yanfeng Chen, Xinhua Feng, Ao Liu, Xingwu Sun, Roberts Wang, Yaping Deng, Suncong Zheng, Guanghui Xu, Junqiang Zheng, Chengzhong Xu, Peijie She, Yao Ding, Zhongzhi Chen, Rongpeng Chen, Zilong Zhao, Saiyong Yang, Zongwei Li, Yuchi Deng, Lulu Wu, Bo Wang, Ze Zhao, Yiqing Huang, Xiaoqin Ren, Yinben Xia, Zhanhui Kang, Wen Ouyang, Rui Yuan, Chong Zha, Meng Chen, Xun Cao, Shihui Hu, Chao Yu, Dong Du, Weijie Liu, Zifan Wu, Hu Chen, Dian Jiao, Qian Wang, Fan Jiang, Huilin Xu, Xipeng Zhang, Tinghao She, Jiajia Wu, Lei Jiang, Decheng Wu, Dengpeng Wu, Yigeng Hong, Xiao Feng, Xirui Li, Rong Gan, Xiong Kuang, Hao Gong, Guiyang Li, Xiaobo Shu, Jiahao Bu, Tao Yang, Yi Shen, Jianchen Zhu, Xiang Li, Jonny Han, Zekun He, Jiaqi Zhu, Shaohua Chen, Chongqing Zhao, Yue Mao, Yuyuan Zeng, Tengfei Cao, Feng Zhang, Zhichao Hu, Liang Dong, Fusheng Xiang, Chengcheng Xu, Weichao Wang, Ruobing Xie, Shuaipeng Li, Yiqi Chen, Feifei Liu, Fengzong Lian

- ***What's New***: 이번 논문은 텐센트에 의해 개발된 Hunyuan-Large를 소개합니다. Hunyuan-Large는 현재 공개된 가장 큰 오픈 소스 Transformer 기반의 혼합 전문가 모델(Mixture of Experts; MoE)로, 3890억 개의 총 파라미터와 520억 개의 활성화 파라미터를 포함하고 있으며 최대 256K 토큰을 처리할 수 있습니다. 다양한 벤치마크에서 뛰어난 성능을 보여 LLama3.1-70B와 LLama3.1-405B 모델에 비해 우수한 성능을 제공합니다.
- ***Technical Details***: Hunyuan-Large는 광범위한 합성 데이터를 사용하여 이전 문헌보다 훨씬 큰 학습 데이터를 마련하고, 혼합 전문가 라우팅 전략과 키-값 캐시 압축 기법을 통해 모델을 향상시켰습니다. 전문가별 학습률 전략도 도입되었습니다. 또한, MoE 모델의 스케일링 법칙과 학습률 스케줄을 조사하여 향후 모델 개발과 최적화를 위한 귀중한 통찰을 제공합니다.
- ***Performance Highlights***: Hunyuan-Large는 다양한 영어 및 중국어 벤치마크에서 최상의 성능을 기록하며, 기존 동급 모델 대비 최고 수준의 수행력을 보여줍니다. 특히, MMLU 벤치마크에서 LLama3.1-405B 모델을 능가하는 성과를 이루었으며, 이는 토큰 활성화 수가 훨씬 적은 상황에서도 달성되었습니다. 또한, 수학적 문제 해결과 코딩 데이터셋에서도 최고 성적을 기록하여 뛰어난 LLM 능력을 입증합니다.

### [From Medprompt to o1: Exploration of Run-Time Strategies for Medical Challenge Problems and Beyond](https://arxiv.org/abs/2411.03590)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.03590.png)

Vote: 8

Authors: Sheng Zhang, Scott Mayer McKinney, Naoto Usuyama, Harsha Nori, Xavier Fernandes, Nicholas King, Eric Horvitz

- ***What's New***: 이 연구는 OpenAI의 새로운 모델 o1-preview가 의료 도전 문제 해결에 있어 Medprompt와 같은 고급 동적 프롬프트 전략을 사용하는 GPT-4 시리즈보다 우수한 성능을 보여준다는 것을 발견했습니다. 특히, o1-preview 모델은 기존 프롬프트 없이도 뛰어난 성능을 발휘하며, 이는 러닝-타임(reasoning before generating final responses)이 내재된 'reasoning-native' 모델의 새로운 패러다임을 제시합니다.
- ***Technical Details***: Medprompt는 다단계 프롬프트(pipeline)을 사용하여 대규모 언어 모델(LLM)의 추론 및 성능을 강화하는 전략입니다. 문제 해결을 단계별로 진행하는 체인 오브 쏘트(chain-of-thought reasoning)와 앙상블 기법(ensembling)을 통한 최적화를 포함하고 있습니다. o1-preview 모델은 GPT-4와 달리 자체적으로 체인 오브 쏘트(reasoning)을 수행할 수 있도록 강화학습(reinforcement learning)으로 훈련되었습니다.
- ***Performance Highlights***: o1-preview 모델은 MedQA와 같은 기존의 의료 벤치마크에서 뛰어난 성능을 보였습니다. 특히 MedQA 결과에서는 이전 모델보다 우수한 정확도(96%)를 기록하며, 다양한 방식으로 최적의 성과를 거두었습니다. 이는 새로운 'reasoning-native' 모델이 고급 프롬프트 기법이 불필요함을 의미하며, 비용 대비 효율성을 고려한 새로운 파레토 경계를 제안합니다.

### [Polynomial Composition Activations: Unleashing the Dynamics of Large Language Models](https://arxiv.org/abs/2411.03884)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.03884.png)

Vote: 17

Authors: Ya Wang, Xun Zhou, Jinwen Ma, Xiaoqing Li, Yutao Zeng, Zhijian Zhuo

- ***What's New***: 이 논문에서는 트랜스포머(Transformers)의 성능을 향상시키기 위해 설계된 새로운 활성 함수 카테고리인 다항식 조합 활성화(Polynomial Composition Activations; PolyCom)을 제안합니다. PolyCom은 ReLU나 GELU와 같은 기존의 활성 함수를 대체하여 트랜스포머 모델이 더 복잡한 데이터 패턴을 모델링할 수 있도록 합니다.
- ***Technical Details***: PolyCom은 다항식과 기타 함수의 조합으로, ReLU 및 전통적 다항식보다 더 강력한 표현 능력을 갖고 Sobolev 공간에서 최적의 근사율을 달성합니다. PolyCom의 두 가지 변종인 PolyReLU와 PolyNorm을 소개하며, 트랜스포머 아키텍처 내 통합을 설명합니다. 이들은 다항식의 각 항의 크기를 일정하게 유지하도록 설계되어 과학적 이론 분석을 통해 트랜스포머의 표현 능력을 향상시키는 것으로 나타났습니다.
- ***Performance Highlights***: 실험 결과, PolyCom을 사용한 대형 언어 모델(LLMs)은 기존의 활성화 함수들을 사용하는 모델에 비해 수렴 속도를 가속화하고 정확도를 높이는 등의 성능 개선을 보였습니다. PolyNorm은 다양한 벤치마크 과제에서 SwiGLU를 포함한 다른 활성화 함수 대비 높은 성능을 지속적으로 나타냈으며, 트랜스포머 모델의 전반적인 표현성과 효율성을 개선했습니다.

### [Training-free Regional Prompting for Diffusion Transformers](https://arxiv.org/abs/2411.02395)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.02395.png)

Vote: 22

Authors: Wenzhao Zheng, Jianjin Xu, Haofan Wang, Yida Wang, Gaole Dai, Anthony Chen, Renrui Zhang, Shanghang Zhang

- ***What's New***: 이 연구에서는 최신 Diffusion Transformer (DiT) 아키텍처인 FLUX.1에 대해 훈련이 필요 없는 지역적 프롬프트(Regional Prompting)를 제안 및 구현했습니다. 이는 FLUX.1 모델이 훈련 없이도 세밀한 조합의 텍스트-이미지 생성 기능을 발휘할 수 있도록 설계되었습니다.
- ***Technical Details***: FLUX.1에서 주목할 점은 MMDiT 구조의 동적 프롬프트 표현 업데이트입니다. 지역 인식 주의 조작(region-aware attention manipulation) 모듈은 네 가지 부분으로 나뉘어 주의기능이 수행되며, 이미지와 텍스트 간의 교차 주의, 이미지 내 자기 주의, 텍스트 내 자기 주의를 포함합니다. 이러한 구조는 조합 생성(compositional generation) 중 각각의 지역텍스트 쌍이 주목 메커니즘에서 적절히 고려되고 이미지의 전체적 특징을 유지하며 불필요한 상호작용을 방지합니다.
- ***Performance Highlights***: 주요 결과는 다양한 시각적 프롬프트를 다루는 데 있어 모델의 적응성과 정밀성을 보여줍니다. 실험은 다양한 지역 마스크 설정에서도 강력한 영역 정렬과 정확한 지역 특성 번역을 유지하며 높은 적합성을 유지하는 모습을 보여줍니다. 또한, 우리의 방법은 RPG 기반의 접근법보다 9배 빠른 추론 속도를 자랑하며, RFID 기반 시스템보다 GPU 메모리 소비량이 적습니다.

### [Zebra-Llama: A Context-Aware Large Language Model for Democratizing Rare Disease Knowledge](https://arxiv.org/abs/2411.02657)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.02657.png)

Vote: 5

Authors: Lashaw Salta, Catalina Villouta, Andrew Langdon, Braian Peetoom, Chinmay Agrawal, Gianmarco Bellucci, Orion J Buske, Karthik Soman

- ***What's New***: Zebra-Llama는 드문 질병 지식을 대중화하기 위해 개발된 새로운 문맥 인식 대형 언어 모델 (Context-Aware Large Language Model)이자 Ehlers-Danlos 증후군(EDS) 관리에 집중된 전문화된 AI 솔루션입니다. 드문 질병 분야의 정보 격차를 줄이기 위한 중요한 진전을 보여주며, EDS관련 질문 처리에서 정확성과 인용 신뢰도를 향상시켰습니다.
- ***Technical Details***: Zebra-Llama는 Retrieval-Augmented Generation (RAG) 기능이 통합된 문맥 인식 미세조정 방법론을 통해 개발되었습니다. 의료 문헌, 환자 경험 및 임상 자원에서 추출한 질문으로 훈련되었으며, 전문가가 큐레이팅한 응답을 포함합니다. 다양한 데이터 소스를 통합하여 구조화된 질문-문맥-답변(Question-Context-Answer) 형태로 데이터를 정리하여 모델을 훈련시켰습니다. 학습 과정에서 Pinecone 벡터 데이터베이스와 OpenAI의 텍스트 임베딩을 사용하여 문맥 관련 정보를 효과적으로 활용하도록 설계되었습니다.
- ***Performance Highlights***: Zebra-Llama는 실제 EDS 관련 질문 세트에서 철저성, 정확성, 명확성 및 인용 신뢰성에서 기본 모델(Llama-3.1-8B-Instruct) 대비 각각 77.5%, 83.0%, 74.7%, 70.6%로 성능을 개선했습니다. 모델이 생성한 응답의 인용 정확도도 크게 개선되어, 응답당 인용 정확도에서 70.4%로 뛰어난 성과를 보였습니다.

### [M3DocRAG: Multi-modal Retrieval is What You Need for Multi-page Multi-document Understanding](https://arxiv.org/abs/2411.04952)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.04952.png)

Vote: 1

Authors: Yujie He, Ozan Irsoy, Mohit Bansal, Jaemin Cho, Debanjan Mahata

- ***What's New***: M3DOCRAG은 문서 기반 시각적 질문 응답(Document Visual Question Answering; DocVQA)에 다중 페이지 및 다중 문서 이해를 위한 새로운 멀티모달 RAG(Multi-modal Retrieval-Augmented Generation) 프레임워크입니다. 기존 방법들이 한 페이지의 문서 또는 텍스트 기반의 수집 생성(Text-based Retrieval-Augmented Generation; RAG)에 의존하는 반면, M3DOCRAG은 다양한 문서 및 시각 정보를 효율적으로 처리할 수 있도록 설계되었습니다.
- ***Technical Details***: M3DOCRAG는 문서의 모든 페이지를 RGB 이미지로 변환하여 시각적 임베딩을 추출하고, ColPali와 같은 다중모달 검색 모델을 사용하여 쿼리와 가장 유사한 페이지를 회수합니다. Query에 대한 답을 생성하기 위해 Qwen2-VL과 같은 멀티모달 언어 모델(MLM)이 사용됩니다. 문서를 닫힌 도메인(특정 문서 내)과 열린 도메인(여러 문서 내) 설정 모두에서 처리할 수 있으며, 시각적 정보가 포함된 페이지를 효율적으로 검색하고 질문에 대한 답을 생성할 수 있습니다.
- ***Performance Highlights***: M3DOCRAG는 M3DOCVQA, MMLongBench-Doc, MP-DocVQA 등 세 가지 벤치마크에서 강력한 성능을 보여주었으며, 특히 MP-DocVQA에서 최첨단 성능을 달성했습니다. M3DOCVQA 데이터셋에서는 멀티모달 RAG가 텍스트 기반 RAG를 뛰어넘어 이미지가 포함된 증거를 사용하는 질문에서 특히 높은 성능 차이를 보였습니다. 다양한 색인(Indexing) 및 모델 설정을 통해 사실상 높은 정확도와 빠른 검색 속도를 구현하였습니다.

### [TIP-I2V: A Million-Scale Real Text and Image Prompt Dataset for Image-to-Video Generation](https://arxiv.org/abs/2411.04709)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.04709.png)

Vote: 10

Authors: Wenhao Wang, Yi Yang

- ***What's New***: TIP-I2V는 최초로 이미지에서 비디오로의 생성(Image-to-Video Generation)을 위한 170만 개 이상의 고유 사용자 제공 텍스트 및 이미지 프롬프트 데이터셋을 도입했습니다. 이 데이터셋은 이미지에서 비디오로의 연구 발전을 지원하며, 모델의 안전성을 높이고자 하는 새로운 연구 방향을 제안합니다.
- ***Technical Details***: TIP-I2V 데이터셋은 5개의 최첨단 이미지-비디오 모델(Pika, Stable Video Diffusion, Open-Sora, I2VGen-XL, CogVideoX-5B)에 의해 생성된 비디오를 포함하고 있습니다. 각 비디오는 100,000개의 무작위로 선택된 프롬프트를 바탕으로 생성되었으며, 텍스트와 이미지 프롬프트, NSFW 점수, UUID, 타임스탬프 등이 함께 제공됩니다. 또한 이 데이터셋은 사용자의 선호 사항을 분석하고 다차원적인 모델 성능 평가를 가능합니다.
- ***Performance Highlights***: TIP-I2V는 기존의 프롬프트 데이터셋인 VidProM 및 DiffusionDB와 비교하여, 텍스트와 이미지 프롬프트를 동시에 제공하여 보다 다양한 프롬프트와 생성된 출력을 포함합니다. 새로운 연구는 특히 사용자 경험을 향상시키고, 평가의 실용성을 개선하며, 생성된 비디오의 안전성을 높이는데 기여할 것으로 기대됩니다. 또한 현재의 이미지-비디오 모델이 사용자 제어와 비디오-텍스트 정렬에서 높은 정확도를 유지하는 데 어려움을 겪고 있음을 시사합니다.

### [Self-Consistency Preference Optimization](https://arxiv.org/abs/2411.04109)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.04109.png)

Vote: 8

Authors: Archiki Prasad, Weizhe Yuan, Sainbayar Sukhbaatar, Jason Weston, Maryam Fazel-Zarandi, Jane Yu, Mohit Bansal, Jing Xu, Richard Yuanzhe Pang

- ***What's New***: 자체 일치(Self-consistency)를 이용하여 모델의 추론 능력을 개선하는 혁신적인 방법인 '자체 일치 선호 최적화(Self-consistency Preference Optimization; SCPO)'가 도입되었습니다. 이는 불확실한 보상 문제를 해결하며, 모델이 복잡한 추론 작업에서 스스로 학습하고 개선할 수 있도록 지원합니다.
- ***Technical Details***: SCPO는 모델이 생성한 응답 중 가장 일치하는 응답을 선호하도록 학습하는 방식입니다. 이는 모델이 생성한 문제에 대해 여러 샘플을 생성하고, 가장 빈도가 높은 응답을 선택하는 방법입니다. 또한, SCPO는 반감없는 손실(Weighted Loss)을 사용하여 응답의 일관성을 기반으로 각 사례에 가중치를 부여하여 최적화를 수행합니다.
- ***Performance Highlights***: SCPO는 GSM8K 및 MATH와 같은 추론 작업에서 0~22.74%의 정확도 향상을, ZebraLogic에서 이미 알려진 더 큰 모델보다 우수한 성능을 보여줍니다. 두 번의 반복 훈련으로, SCPO는 대체로 감독학습과 비슷한 성능을 달성하며 일부 실험에서는 IRPO 같은 기존 방법보다 우월한 성과를 거두었습니다.

### [DynaSaur: Large Language Agents Beyond Predefined Actions](https://arxiv.org/abs/2411.01747)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.01747.png)

Vote: 13

Authors: Trung Bui, Puneet Mathur, Nedim Lipka, Viet Dac Lai, Seunghyun Yoon, Handong Zhao, Franck Dernoncourt, Yu Wang, Tianyi Zhou, Ryan A. Rossi, Dang Nguyen, Ruiyi Zhang

- ***What's New***: DynaSaur는 고정된 행동 집합을 넘어서 동적 행동 생성과 결합을 가능하게 하는 LLM 에이전트 프레임워크를 제안합니다. 이는 에이전트가 일반적인 프로그래밍 언어에서 작성된 프로그램을 생성 및 실행함으로써 환경과 상호작용할 수 있도록 하며, 생성된 행동을 재사용하기 위해 누적합니다.
- ***Technical Details***: DynaSaur는 각 행동을 파이썬 함수로 모델링하여 행동의 보편적 표현을 확보합니다. 에이전트는 부족한 경우 새로운 함수를 정의하고, 기존 함수를 재사용하는 방식으로 Python 코드를 생성하여 행동을 수행합니다. 환경 내부에서 코드는 Python 인터프리터를 통해 실행되며, 관찰 결과가 에이전트에 반환됩니다. 모든 생성 행동은 누적되어 미래에 사용할 수 있는 라이브러리를 구축합니다.
- ***Performance Highlights***: GAIA 벤치마크에서의 광범위한 실험은 DynaSaur 프레임워크가 훨씬 더 유연하며 이전 방법들보다 뛰어난 성능을 발휘함을 보여줍니다. 특정 시나리오에서 미리 정의된 행동 집합에는 없는 상황에서도 새로운 행동을 생성하여 회복할 수 있으며, GAIA 공개 리더보드에서 최고의 위치를 차지했습니다.

### [Thanos: Enhancing Conversational Agents with Skill-of-Mind-Infused Large Language Model](https://arxiv.org/abs/2411.04496)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.04496.png)

Vote: 10

Authors: Kyeongjin Oh, Junyoung Youn, Ho-Jin Choi, Young-Jun Lee, Dokyong Lee

- ***What's New***: THANOS는 대화형 에이전트의 응답 품질을 개선하기 위해 Skill-of-Mind 개념을 도입한 대규모 언어 모델(LLM) 기반의 새로운 모델군입니다. 이는 사용자와의 사회적 상호작용 시 복잡한 대화 속에서 적절한 대화 기술을 선택할 수 있도록 설계되었습니다. 새로운 데이터셋인 MULTIFACETED SKILL-OF-MIND를 기반으로 다양한 상호작용 시나리오에 걸쳐 여러 대화 기술을 포함하고 있습니다.
- ***Technical Details***: THANOS는 1B, 3B, 8B 파라미터 모델로 구성되어 있습니다. 이번 연구는 MULTIFACETED SKILL-OF-MIND라는 대화 데이터셋을 기반으로 기술-of-mind을 주입하여 LLMs의 대화 능력을 강화합니다. 이 데이터셋은 10만 개의 대화를 포함하며, 다양한 대화 기술과 설명이 주석으로 포함되어 있습니다. THANOS는 각 대화 기술 예측과 설명 생성을 통해 일반화 능력을 발휘하며, 다양한 사회적 상황에서 효과적으로 대응합니다.
- ***Performance Highlights***: THANOS는 기존 LLM 기반 대화 에이전트들에 비해 속마음을 유추하는 측면에서 뛰어난 성능을 보여줍니다. 새로운 모델들은 실험 결과에서 다중 시나리오에 대한 일반화 성능을 입증하였으며, 응답 생성 품질이 크게 향상되었습니다. 그러나 특정성 측면에서는 개선 효과가 미미하여, 향후 연구에서 보완이 필요할 것으로 보입니다.

### [OpenCoder: The Open Cookbook for Top-Tier Code Large Language Models](https://arxiv.org/abs/2411.04905)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.04905.png)

Vote: 55

Authors: Yang Xu, Qian Liu, Siming Huang, Liuyihan Song, Jiaran Hao, Jie Fu, Yinghui Xu, Yuan Qi, Ge Zhang, Jason Klein Liu, Tianhao Cheng, J. Yang, J. H. Liu, Zhaoxiang Zhang, Zili Wang, Linzheng Chai, Chenchen Zhang, Ruifeng Yuan, Wei Chu

- ***What's New***: OpenCoder는 고급 코드 대형 언어 모델(Code Large Language Models; LLMs)을 구축하기 위한 '오픈 요리책'을 제공합니다. 기존 모델과 유사한 성능을 달성하면서도 연구 커뮤니티에 재현 가능한 데이터 처리 파이프라인과 투명한 훈련 프로토콜을 함께 공개함으로써 큰 기반을 제공합니다.
- ***Technical Details***: OpenCoder는 960억 개의 토큰을 포함하는 RefineCode 데이터셋을 사용하여 개발되었습니다. 데이터는 주로 GitHub 저장소와 웹 데이터에서 수집되었으며, 파일 수준의 중복 제거와 언어별 맞춤 규칙을 적용하여 데이터 품질을 높였습니다. 또한, Python, Java 등 다양한 프로그래밍 언어에 대한 데이터가 고르게 포함되어 있습니다.
- ***Performance Highlights***: OpenCoder-8B 모델은 HumanEval, MBPP 등 여러 코드 생성 평가 벤치마크에서 우수한 성능을 보였으며, 특히 Reproducible Datasets과 함께 제공하여 현재까지 공개된 오픈 모델 중 최고의 성능을 나타냈습니다. HumanEval에서의 점수는 이전의 오픈 소스 모델들보다 뛰어났습니다.

### [SG-I2V: Self-Guided Trajectory Control in Image-to-Video Generation](https://arxiv.org/abs/2411.04989)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.04989.png)

Vote: 6

Authors: Yash Kant, Igor Gilitschenski, Koichi Namekata, David B. Lindell, Ziyi Wu, Sherwin Bahmani

- ***What's New***: SG-I2V는 이미지에서 비디오 생성 시 객체와 카메라의 움직임을 제어할 수 있는 시스템을 제안하며, 이는 사전에 학습된 이미지-비디오 확산 모델(image-to-video diffusion model)의 지식을 활용하여 제로샷(Zero-Shot) 방식으로 동작합니다. 즉, 외부 지식이나 미세 조정을 필요로 하지 않으면서 이동 궤적을 제어할 수 있는 기능을 제공합니다.
- ***Technical Details***: SG-I2V는 사전 학습된 이미지-to-비디오 확산 모델인 안정적 비디오 확산 모델(Stable Video Diffusion; SVD) 기반으로 구축되었으며, 초기에 메타포 정보의 배열을 분석하여 기능 맵(feature map)을 정렬하는 새로운 방법을 사용합니다. 그 후, 노이즈 초기화 단계의 voxel 내에서 기능 유사성을 보존하기 위한 최적화 기술을 적용하며, 마지막으로 고주파 성분 보존을 통해 비디오의 시각적 품질을 향상시키는 후처리를 실현합니다.
- ***Performance Highlights***: SG-I2V는 제로샷 방식임에도 불구하고 감독 학습된 모델과 시각적 품질과 움직임 충실도 측면에서 경쟁력 있는 성능을 발휘합니다. VIPSeg 데이터셋에서 FID 점수가 28.87, FVD 점수가 298.10, 그리고 ObjMC가 14.43으로 측정되어 기존의 제로샷 기법들보다 우수한 결과를 보였습니다.

### [MVPaint: Synchronized Multi-View Diffusion for Painting Anything 3D](https://arxiv.org/abs/2411.02336)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.02336.png)

Vote: 23

Authors: Bin Fu, Chi Zhang, Xin Chen, Gang Yu, Ziwei Liu, Liang Pan, Xianfang Zeng, Anqi Pang, Wei Cheng, Zhibin Wang, Juncheng Mu

- ***What's New***: MVPaint는 3D 텍스처 생성에서 다중 뷰를 동기화하는 새로운 프레임워크를 제공합니다. 이 프레임워크는 복잡한 UV 언래핑에 강하고 고해상도의 끊김 없는 텍스처를 생성할 수 있습니다.
- ***Technical Details***: MVPaint는 세 가지 주요 모듈로 구성되어 있습니다. (1) Synchronized Multi-view Generation(SMG) 모델은 다중 뷰 이미지를 동시에 생성하여 초기 텍스처를 만듭니다. (2) Spatial-aware 3D Inpainting(S3I) 모듈은 관찰되지 않은 영역의 텍스처를 보강합니다. (3) UV Refinement(UVR) 모듈은 UV 공간에서 슈퍼해상도 및 공간 인식 Seam-Smoothing 알고리즘을 사용합니다.
- ***Performance Highlights***: MVPaint는 Objaverse와 GSO T2T 벤치마크에서 기존 최신 방법들보다 성능이 우수하며, 특히 높은 충실도의 텍스처를 생성하고 시각적으로 일관성이 뛰어납니다.

### [GenXD: Generating Any 3D and 4D Scenes](https://arxiv.org/abs/2411.02319)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.02319.png)

Vote: 16

Authors: Gim Hee Lee, Chung-Ching Lin, Jianfeng Wang, Yuyang Zhao, Kevin Lin, Zhiwen Yan, Lijuan Wang, Zhengyuan Yang, Linjie Li

- ***What's New***: GenXD는 다양한 조건 이미지를 기반으로 고품질의 3D 및 4D 장면 생성을 가능하게 하는 통합 모델입니다. 이 모델은 카메라 및 오브젝트 이동을 분리하여 학습할 수 있으며, 여러 응용 분야에서 강력한 성능을 보입니다. 특히 대규모 4D 장면 데이터세트인 CamVid-30K를 소개하여 4D 데이터 부족 문제를 해결합니다.
- ***Technical Details***: GenXD는 다중뷰-시간 모듈(multiview-temporal modules)을 활용해 3D와 4D 데이터를 통합하여 학습합니다. 카메라와 오브젝트 이동을 분리해 학습하며, 마스크된 잠재 조건(masked latent conditioning)을 사용해 여러 조건의 입력 이미지를 지원합니다. 카메라 조건은 Plücker ray를 사용하고, 3D와 4D 데이터는 모듈 학습 중 분리 및 통합이 이루어집니다.
- ***Performance Highlights***: GenXD는 단일 및 다중보기 생성 조건을 모두 지원하며, 기존의 3D 및 4D 생성 방법보다 우수하거나 동등한 성능을 보입니다. 4D 장면 생성에서 FID 및 FVD 평가 지표에서 CameraCtrl 및 MotionCtrl보다 우수한 성능을 기록하였으며, 몇 개의 보기에서 3D 복원 성능은 기존 방법에 비해 PSNR, SSIM, LPIPS 지표가 향상되었습니다.

### [AndroidLab: Training and Systematic Benchmarking of Android Autonomous Agents](https://arxiv.org/abs/2410.24024)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2410.24024.png)

Vote: 45

Authors: Hanyu Lai, Xueqiao Sun, Hao Yu, Yifan Xu, Jie Tang, Yuxiao Dong, Siyi Cheng, Dan Zhang, Shudan Zhang, Xiao Liu

- ***What's New***: AndroidLab는 안드로이드 자율 에이전트(Android Autonomous Agents)의 체계적 훈련과 벤치마크(Benchmark)를 위한 새로운 프레임워크입니다. 이 프레임워크는 다양한 모달리티를 지원하는 운영 환경과 재현 가능한 벤치마크를 포함하며, 동일한 액션 스페이스에서 대형 언어 모델(LLMs)과 멀티모달 모델(LMMs)을 지원합니다.
- ***Technical Details***: AndroidLab 벤치마크는 안드로이드 가상 디바이스를 이용하여 구축된 9개의 앱에서 138개의 작업을 포함합니다. 각 작업은 여러 페이지 상태로 나누어져 하위 목표(Sub-Goal)를 설정하며, UI 트리 구조의 일치 여부로 정확한 탐색을 검증합니다. 이 프레임워크는 새로운 XML 및 SoM 모드 외에도 ReAct와 SeeAct 프레임워크를 구현하여 에이전트가 환경을 관찰하고 반응할 수 있도록 합니다.
- ***Performance Highlights***: 안드로이드 가상 환경에서 GPT-4o 모델은 XML 모드와 SoM 모드에서 성공률(Success Rate) 31.16%를 기록하여 다른 모델을 능가했습니다. 반면에 오픈 소스 모델 들은 향상된 훈련 없이 약 5%의 낮은 성공률을 보였지만, Android Instruct 데이터셋으로 세밀 조정을 통해 GLM4-9B 모델의 성공률은 21.01%로 증가했습니다. XML+ReAct 모드에서 GPT-4o의 성능은 33.33%의 성공률로 개선되었습니다.

### [Large Language Models Orchestrating Structured Reasoning Achieve Kaggle Grandmaster Level](https://arxiv.org/abs/2411.03562)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.03562.png)

Vote: 36

Authors: Refinath Shahul Hameed Nabeezath Beevi, Khyati Khandelwal, Albert Thomas, Jianye Hao, Jun Yao, Haitham Bou-Ammar, Ignacio Iacobacci, Jun Wang, Balazs Kegl, Hamza Cherkaoui, Abdelhakim Benechehab, Antoine Grosnit, Alexandre Maraval, Giuseppe Paolo, Jonas Gonzalez, James Doran, Youssef Attia El-Hili, Kun Shao

- ***What's New***: Agent K v1.0은 다양한 데이터 과학 작업을 자동화, 최적화 및 일반화하도록 설계된 최초의 엔드-투-엔드 자동 데이터 과학 에이전트입니다. 이 에이전트는 유연한 구조적 추론 프레임워크를 활용하여 경험에서 학습하며, 이를 통해 복잡한 추론 작업을 처리할 수 있습니다. Agent K는 카글(Kaggle) 경진대회에서 인간 경쟁자들과의 성과 비교를 통해 그 능력을 입증합니다.
- ***Technical Details***: Agent K v1.0은 경험적 학습을 통해 데이터 과학 작업의 전 과정을 관리합니다. Bayesian 최적화 및 고급 특징 공학과 같은 기법을 사용하여 모델을 최적화하고 Torchvision 및 HuggingFace와 같은 라이브러리를 통합하여 다양한 데이터 모달리티를 처리합니다. 수집부터 결과 제출까지의 프로세스를 엄격히 평가하여 엔드-투-엔드 능력을 검증합니다.
- ***Performance Highlights***: Agent K v1.0은 다양한 카글 경진대회에서 92.5%의 성공률을 기록하며상위 38%의 Elo-MMR 점수를 달성했습니다. 이 점수는 인간 그랜드마스터가 달성한 점수의 1사분위와 3사분위 사이에 위치합니다. Agent K는 현재 카글 그랜드마스터 수준의 성과를 기록하며 총 6개의 금메달, 3개의 은메달, 7개의 동메달을 획득하였습니다.

### [HtmlRAG: HTML is Better Than Plain Text for Modeling Retrieved Knowledge in RAG Systems](https://arxiv.org/abs/2411.02959)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.02959.png)

Vote: 51

Authors: Wen Wang, Mang Wang, Jiejun Tan, Weipeng Chen, Zhicheng Dou, Ji-Rong Wen

- ***What's New***: HtmlRAG는 RAG 시스템에서 HTML을 외부 지식 형식으로 사용하여 정보 손실을 줄이고 구조적 및 의미적 정보의 보존을 강화합니다. 이는 RAG 프로세스에서 일반적으로 사용되는 플레인 텍스트 대신 HTML 형식을 채택하여 유익한 정보를 유지하려는 최초의 시도입니다.
- ***Technical Details***: HtmlRAG는 HTML을 사용하는 새로운 접근 방식으로, HTML 청소 모듈과 이중 단계 블록 트리 기반 가지치기(Pruning) 방법을 제안합니다. 청소 단계에서는 CSS와 JavaScript 같은 불필요한 내용을 제거하고 구조적인 중복을 줄이며, 블록 트리 기반 가지치기 단계에서는 텍스트 임베딩(Text Embedding)과 생성 모델을 활용하여 관련 없는 HTML 블록을 제거하고 필수 정보를 압축합니다.
- ***Performance Highlights***: 여섯 개의 QA 데이터셋 실험에서 HtmlRAG는 플레인 텍스트 기반의 기존 RAG 시스템 대비 HTML을 활용한 새로운 접근 방식이 탁월한 성능을 보여줬습니다. 특히, LLM 성능 향상과 함께 HTML 형식이 외부 지식로서 적합함을 확인했습니다.

### [DeeR-VLA: Dynamic Inference of Multimodal Large Language Models for Efficient Robot Execution](https://arxiv.org/abs/2411.02359)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.02359.png)

Vote: 12

Authors: Gao Huang, Yulin Wang, Shiji Song, Yang Yue, Shenzhi Wang, Yizeng Han, Jiashi Feng, Bingyi Kang

- ***What's New***: DeeR-VLA는 로봇의 멀티태스크 수행을 위한 멀티모달 대형 언어 모델(MLLMs; Multimodal Large Language Models)의 동적 추론을 제안합니다. 이는 대부분의 로봇 제어 절차가 상대적으로 쉬운 상황으로 구성되어 있으며, 이러한 상황에서는 작은 모델로도 적절한 로봇 동작을 획득할 수 있다는 점에 착안하여 설계되었습니다.
- ***Technical Details***: 새로운 다이나믹 얼리-엑시트 프레임워크(DeeR)는 로봇 비전-언어-액션 모델을 위한 구조로, 상황에 따라 활성화되는 MLLM의 크기를 자동으로 조정합니다. 이를 위해 다양한 종료점을 갖춘 다중 엑시트 아키텍처를 활용하여 불필요한 연산을 줄이고, 사전 정의된 요구 조건에 따라 조기 종료 기준을 정립하여 GPU 메모리 사용을 효율화합니다. 또한, 시퀀스 중심의 최적화된 훈련 방법도 개발하여 시간 정보를 통합하고 합리적인 동작 예측을 지원합니다.
- ***Performance Highlights***: CALVIN 로봇 조작 벤치마크에서 DeeR는 LLM의 연산 비용을 5.2-6.5배, GPU 메모리 사용을 2-6배 줄이면서도 성능 저하 없이 효율적인 운영을 달성했습니다. 또한, 시뮬레이션 환경에서 OpenFlamingo 9B 모델을 확장했을 때 1.8-5.7배의 연산 감소 효과를 보였습니다.

### [LoRA-Contextualizing Adaptation of Large Multimodal Models for Long Document Understanding](https://arxiv.org/abs/2411.01106)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.01106.png)

Vote: 4

Authors: Yufan Zhou, Tong Sun, Tong Yu, Jiuxiang Gu, Franck Dernoncourt, Jian Chen, Changyou Chen, Ryan A. Rossi, Ruiyi Zhang

- ***What's New***: 이 논문에서는 장문서 이해를 위한 대형 멀티모달 모델(Large Multimodal Models; LMMs)의 적응을 위해 LoRA-Contextualizing Adaptation of Large multimodal models (LoCAL)라는 새로운 프레임워크를 소개합니다. 이 프레임워크는 LMM의 긴 문서 처리를 지원하며, 효율적인 증거 페이지 검색(evidence page retrieval)과 질의 응답(question answering)을 위해 두 가지 LMM 어댑터를 사용합니다.
- ***Technical Details***: LoCAL은 증거 페이지 검색과 질문 응답을 위한 두 가지 모듈로 구성된 모델 아키텍처를 소개합니다. Col-retrieval 모듈은 시각적 임베딩을 계산하고 텍스트 임베딩과 결합하여 LLM(대형 언어 모델)을 통해 처리하며, 마지막 숨김 상태(hidden states)를 저차원 특징 공간으로 변환하여 질의 텍스트와 페이지 이미지의 관련성을 측정하는 방법을 사용합니다. 이는 얕은 대화 구조를 기반으로 한 유사성 점수를 사용하여 문서 내에서 가장 관련성이 높은 페이지를 선택합니다.
- ***Performance Highlights***: LoCAL은 4B 파라미터로, 상태-of-the-art 성능을 실현하며 SP-SlideVQA 같은 단일 페이지 질문에서 높은 정확도를 기록했습니다. 또한, MMLongBench-Doc와 같은 다페이지 문서에서도 경쟁력 있는 성능을 보여주며 오픈 소스 모델들 중 최고의 성능을 자랑합니다. 특히 문서의 길이가 긴 경우에도 메모리 사용량과 계산 비용을 최대한 줄이는 방식으로 효율적인 수행이 가능하다는 점이 입증되었습니다.

### [Mixture-of-Transformers: A Sparse and Scalable Architecture for Multi-Modal Foundation Models](https://arxiv.org/abs/2411.04996)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.04996.png)

Vote: 14

Authors: Srinivasan Iyer, Gargi Ghosh, Weixin Liang, Ning Dong, Mike Lewis, Liang Luo, Xi Victoria Lin, Lili Yu, Luke Zettlemoyer, Chunting Zhou, Wen-tau Yih

- ***What's New***: Mixture-of-Transformers (MoT)는 멀티모달 기초 모델을 위한 희소하고 확장 가능한 새로운 트랜스포머 아키텍처입니다. MoT는 모달리티별로 비임베딩 파라미터를 분리하여 텍스트, 이미지, 음성 등 다양한 모달리티를 처리할 수 있도록 설계되었습니다.
- ***Technical Details***: MoT는 글로벌 셀프 어텐션을 활용하여 전체 입력 시퀀스에 대해 모달리티 특정 파라미터를 적용합니다. 다양한 실험 설정에서 테스트된 MoT 모델은 피드포워드 네트워크, 어텐션 행렬 및 레이어 노말라이제이션과 같은 트랜스포머의 비임베딩 파라미터를 모달리티에 맞춰 개별적으로 처리합니다.
- ***Performance Highlights***: Chameleon 설정(자가회귀 텍스트 및 이미지 생성)에서 MoT는 드는 모델의 성능과 동등한 성능을 55.8%의 FLOPs만으로 달성했습니다. 또한, 음성을 포함한 경우에는 37.2%의 FLOPs로 드는 성능에 필적하는 성과를 냈습니다. Transfusion 설정에서 MoT는 1/3의 FLOPs로 이미지 모달리티 성능에서 드는 모델을 능가했습니다. 시스템 프로파일링에서 MoT는 드는 수준의 이미지 품질을 47.2%의 월-클록 시간과 텍스트 품질을 75.6%의 월-클록 시간에 달성했습니다.

### [Adaptive Length Image Tokenization via Recurrent Allocation](https://arxiv.org/abs/2411.02393)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.02393.png)

Vote: 11

Authors: Shivam Duggal, Phillip Isola, William T. Freeman, Antonio Torralba

- ***What's New***: 이번 논문은 2D 이미지에 대해 가변길이 토큰(variable-length tokens) 표현을 학습하는 접근법을 제안합니다. 이는 기존의 고정된 이미지 표현과 달리, 이미지의 엔트로피(entropy), 문맥(context), 친숙도(familiarity)에 따라 가변적인 표현 역량을 부여합니다. 이러한 접근은 객체나 부분의 발견을 위한 가능성을 열어줍니다.
- ***Technical Details***: 제안된 시스템은 반복적인(recurrent) 처리 과정을 통해 2D 이미지 토큰을 1D 잠재(latent) 토큰으로 증류(distillation)합니다. 이 과정은 몇 차례의 반복을 거치며 각 반복에서 2D 토큰을 세분화하고, 기존 1D 잠재 토큰을 업데이트하며 새로운 토큰을 추가하여 표현 역량을 적응적으로 확장합니다. 또한, 이미지 엔트로피(entropy)와 친숙도(familiarity)에 맞춰 가변 토큰 수를 제공하며, 자기 지도 학습(self-supervised learning)을 통해 학습됩니다.
- ***Performance Highlights***: 제안된 ALIT(Adaptive Length Image Tokenizer)은 ImageNet-1K와 같은 대규모 데이터셋의 선형 탐색(linear probing)을 통해 기존의 1D 고정 토크나이저와 비슷한 성능을 보이며, 토큰의 수가 적을수록 강한 모델에서 성능 저하가 더 크게 나타났습니다. 토큰 수는 작업의 복잡성, 친숙도, 하향식 모델 요구사항에 맞춰 조정될 수 있습니다.

### [Needle Threading: Can LLMs Follow Threads through Near-Million-Scale Haystacks?](https://arxiv.org/abs/2411.05000)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.05000.png)

Vote: 7

Authors: Samuel Albanie, Kai Han, Jonathan Roberts

- ***What's New***: 이 연구는 긴 문맥 내에서 정보를 추적하고 복원하는 능력을 평가하는 새로운 테스트 셋을 도입하여 17개의 주요 대형 언어 모델(LLMs)의 문맥 사용 효율성을 분석합니다. 'Long context models'의 성장이 빠르게 진행되는 가운데, 이러한 모델이 얼마나 효과적으로 문맥을 활용하는지 이해하기 위한 체계적 실험이 없다면 한계가 있다는 점을 강조합니다.
- ***Technical Details***: 'Needle Threading'라는 새로운 작업을 도입하여 단일 확인 열쇠 조회 및 복잡한 다중 스레드 추적을 포함한 다양한 난이도의 검색 작업을 통해 모델을 평가합니다. UUID 기반의 문자열을 활용하여 노이즈 없는 실험 데이터를 생성하고 다양한 문맥 길이에서 실험을 수행하며, API를 통해 정보 검색 정확도를 측정합니다.
- ***Performance Highlights***: 여러 모델들이 문맥의 길이에 관계없이 다중 정보를 효과적으로 추적할 수 있는 능력을 보여주었지만, 문맥 길이가 길어질수록 대부분의 모델에서 정확도가 감소한다는 점이 관찰되었습니다. GPT-4o와 Jamba-1.5 Large 모델은 최고의 성능을 기록했으며 일부 모델은 문맥 사용이 제한적이라는 결과를 보였습니다.

### [Constrained Diffusion Implicit Models](https://arxiv.org/abs/2411.00359)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.00359.png)

Vote: 5

Authors: Vivek Jayaram, Ira Kemelmacher-Shlizerman, Steven M. Seitz, John Thickstun

- ***What's New***: CDIM(Constrained Diffusion Implicit Models)은 미리 학습된 확산 모델을 사용하여 노이즈가 존재하는 선형 역문제를 효율적으로 해결하는 새로운 알고리즘을 제안합니다. 이 방법은 디노이징 확산 암시적 모델(DDIM)을 확장하여 출력의 측정 제약을 직접적으로 결합합니다. 여러 과제에 대해 실험을 진행한 결과, CDIM은 기존 조건부 확산 방법보다 10배에서 50배 더 빠른 유추 가속을 보여주었습니다.
- ***Technical Details***: CDIM은 주어진 소음 분포의 잔차 분포에 대한 정확한 제약을 만족시키기 위해 Kullback-Leibler(KL) 발산을 최적화하여 노이즈 케이스를 다룹니다. 또한, 이 접근법은 GAUSIAN 외의 잡음을 포함하는 일반적인 노이즈 모델을 다룰 수 있습니다. CDIM은 상자 인페인팅, 이미지 복원 등 다양한 문제에 적용되며, 각 작업 당 총 10에서 50배의 시간 속도 향상을 입증했습니다.
- ***Performance Highlights***: FFHQ 및 ImageNet 데이터셋에서 CDIM은 FID 및 LPIPS 기준에서 경쟁자들과 비교해 우수한 성과를 보였습니다. 특히 CDIM 모델은 매우 빠른 유추 속도로 주목할 만한 성능 향상을 나타냈으며, 최적화 및 디노이징 단계를 잘 조합하여 뛰어난 품질의 결과를 생성했습니다.

### [PPLLaVA: Varied Video Sequence Understanding With Prompt Guidance](https://arxiv.org/abs/2411.02327)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.02327.png)

Vote: 10

Authors: Haoran Tang, Ying Shan, Ruyang Liu, Chen Li, Jiankun Yang, Haibo Liu, Yixiao Ge

- ***What's New***: PPLLaVA는 새로운 포괄적 비디오 시퀀스 이해 모델로, 프롬프트 가이드를 통해 다양한 길이의 비디오를 이해하는데 초점을 맞추고 있습니다. 이 모델은 기존의 비디오 LLM에서 해결하지 못했던 긴 비디오와 짧은 비디오 모두를 효과적으로 처리할 수 있도록 설계되었습니다.
- ***Technical Details***: PPLLaVA는 시각적 프롬프트 정렬(Visual-Prompt Alignment)을 통해 사용자가 제시한 프롬프트에 관련된 시각적 정보를 추출합니다. 프롬프트 가이드 풀링(Prompt-Guided Pooling)을 사용해 3D 컨볼루션 스타일로 시각적 토큰을 임의의 스케일로 압축하고, 클립 컨텍스트 확장은 긴 대화에서 텍스트 인코딩 능력을 확장합니다.
- ***Performance Highlights***: PPLLaVA는 MSRVTT, MSVD, ActivityNet과 같은 다양한 비디오 벤치마크에서 최첨단 성능을 보여주었으며, 캐릭터 설명, 멀티플 초이스 질문과 같은 다양한 작업에서 뛰어난 결과를 보였습니다. 특히 긴 비디오 이해에서도 새로운 기록을 세웠으며, 기존의 다른 비디오 LLM과 비교할 때 약 7배의 반응 속도를 자랑합니다.

### [LLaMo: Large Language Model-based Molecular Graph Assistant](https://arxiv.org/abs/2411.00871)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.00871.png)

Vote: 18

Authors: Dohwan Ko, Jinyoung Park, Hyunwoo J. Kim, Minseong Bae

- ***What's New***: LLaMo는 대형 언어 모델을 기반으로 한 최초의 분자 그래프 어시스턴트로, 분자 도메인 내에서 언어와 그래프 모달리티 간의 차이를 해소하기 위해 멀티 레벨 그래프 프로젝터를 도입하였습니다. 이는 GNN(Graph Neural Network) 레이어의 출력과 모티프 표현을 교차 주의 메커니즘으로 추상화하여 그래프 표현을 그래프 토큰으로 변환합니다.
- ***Technical Details***: LLaMo 모델은 분자 그래프 인코더, 대형 언어 모델(Large Language Model; LLM), 그리고 멀티 레벨 그래프 프로젝터로 구성됩니다. 이 시스템은 1D SMILES, 2D 분자 그래프, 텍스트를 입력 모달리티로 활용하며, 자동 회귀적으로 텍스트 응답을 생성합니다. LLaMo의 학습은 두 단계로 진행되며, 첫 번째 단계는 분자 그래프-언어 정렬을, 두 번째 단계는 GPT-생성 데이터셋을 사용한 instruction tuning을 포함합니다.
- ***Performance Highlights***: LLaMo는 다양한 작업에서 뛰어난 성능을 보여주며, 기존의 LLM 기반 작업들, 예를 들어 GPT-4, Mol-Instructions와 비교하여 분자 설명 생성, 속성 예측, IUPAC 이름 예측 작업에서 우수한 결과를 나타냅니다. 특히, 다양한 데이터세트와 작업에 대해 일관되게 탁월한 성능을 기록했고, GPT-4 (ICL) 대비 BLEU-4와 METEOR 점수에서 11.9, 14.9점의 개선을 보였습니다.

### [M3SciQA: A Multi-Modal Multi-Document Scientific QA Benchmark for Evaluating Foundation Models](https://arxiv.org/abs/2411.04075)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.04075.png)

Vote: 2

Authors: Ziyao Shangguan, Yixin Liu, Deyuan Li, Arman Cohan, Chuhan Li, Yilun Zhao

- ***What's New***: M3SciQA는 다중 모달 및 다큐먼트 기반의 과학적 질문 답변(Scientific Question Answering; QA)을 평가하기 위한 새로운 벤치마크를 제공합니다. 이는 기존의 단일 문서, 텍스트 중심의 평가 방식을 넘어, AI 모델들이 다수의 자료를 기반으로 비텍스트 데이터를 해석하고 정보를 통합하는 복잡한 연구 워크플로우를 시뮬레이션하도록 설계되었습니다.
- ***Technical Details***: M3SciQA 벤치마크는 70개의 자연어 처리(NLP) 논문 클러스터를 아우르며, 각 클러스터는 주요 논문과 인용된 문서들로 구성되어 있습니다. 이 벤치마크는 총 1,452개의 전문가 주석 질문을 통해 다중 모달 정보 검색과 과학적 문서 전반에 걸친 추론 능력을 평가합니다. 다양한 대형 언어 모델(LLM) 및 다중 모달 모델(LMM)을 대상으로 광범위한 평가를 진행하여 모델의 한계를 분석합니다.
- ***Performance Highlights***: 최고 성능의 모델인 GPT-4o는 사람이 수행한 것과 비교하여 평균 상호 순위(MRR)가 0.488이며, 이는 인간 전문가 기준 0.796에 비해 큰 성능 격차를 보여줍니다. 오픈 소스 및 독점 LMM 모두 이미지 번역 및 재배치 작업에서 한계를 보였으며 장거리 정보 검색에서도 도전 과제에 직면하고 있습니다. 특히, Command R+는 인간 전문가의 76.561 정확도에 비해 33.25의 낮은 정확도를 기록했습니다.

### [DreamPolish: Domain Score Distillation With Progressive Geometry Generation](https://arxiv.org/abs/2411.01602)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.01602.png)

Vote: 9

Authors: Ziqi Cai, Wendi Zheng, Jie Tang, Yuxiao Dong, Yean Cheng, Boxin Shi, Ming Ding, Shiyu Huang

- ***What's New***: DreamPolish는 텍스트-3D 생성 모델로, 진보된 기하학적 세부사항과 포토리얼리스틱한 텍스처를 특징으로 하는 3D 객체를 만드는 데 우수한 성능을 보입니다. 기하학 생성에서는 복수의 neural representation을 이용해 안정성을 높이며, 표면 polishing 단계를 추가하여 이전 단계의 제한된 가이던스에서 기인하는 아티팩트를 정제합니다.
- ***Technical Details***: DreamPolish의 작업은 두 단계로 구성됩니다: progressive geometry polishing과 domain-guided texture enhancing. Geometry 생성에서는 NeRF와 같은 다양한 neural representation을 교차하며 사용하고, NeuS 및 DMTet로 점차 발전시킵니다. Texture 생성에서는 Domain Score Distillation (DSD) 목적을 도입하여 neural representation을 photorealistic한 렌더링을 포함하는 domain으로 안내합니다.
- ***Performance Highlights***: DreamPolish는 포토리얼리스틱 텍스처와 매끄러운 표면의 3D 객체를 생성하는 데 있어 기존 모델을 능가하며, 특히 CLIP Score 및 PSNR, SSIM와 같은 측정지표에서 높은 성능을 보였습니다. 사용자 연구 결과, 사용자들은 DreamPolish가 가장 우수한 성능을 보였다고 평가했습니다.

### [ReCapture: Generative Video Camera Controls for User-Provided Videos using Masked Video Fine-Tuning](https://arxiv.org/abs/2411.05003)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.05003.png)

Vote: 37

Authors: David Junhao Zhang, Roni Paiss, Nikhil Karnad, David E. Jacobs, Nataniel Ruiz, Shiran Zada, Yael Pritch, Mike Zheng Shou, Neal Wadhwa, Inbar Mosseri

- ***What's New***: ReCapture는 사용자 제공 비디오로부터 새로운 카메라 경로를 생성하는 방법을 소개합니다. 이 방법은 기존의 장면 움직임을 보존하면서도 참조 비디오에서 볼 수 없는 각도에서 시청할 수 있는 새로운 비디오를 생성합니다.
- ***Technical Details***: ReCapture는 다중 뷰 확산 모델(multiview diffusion models)이나 깊이 기반 포인트 클라우드 렌더링(depth-based point cloud rendering)을 사용해 새로운 카메라 경로를 가진 노이즈 앵커 비디오(anchor video)를 생성하고, 이후 제안된 마스킹 비디오 파인 튜닝 기법(masked video fine-tuning)을 통해 깨끗하고 일관된 비디오로 재생성합니다. 공간 LoRA와 시간적 모션 LoRA를 비디오 확산 모델의 적절한 층(temporal layers)에서 트레이닝하여 알려진 픽셀과 참조 프레임 데이터를 기반으로 새로운 장면 움직임을 학습합니다.
- ***Performance Highlights***: ReCapture는 4D 데이터셋 없이도 쌍의 비디오 데이터가 요구되는 기존 방법들보다 성능이 뛰어나며, Kubric 데이터셋에서 방법론의 뛰어난 성능을 보여줍니다. VBench에서 여러 평가 차원에서 다른 방법들보다 우수한 성과를 기록했습니다.

### [Swan and ArabicMTEB: Dialect-Aware, Arabic-Centric, Cross-Lingual, and Cross-Cultural Embedding Models and Benchmarks](https://arxiv.org/abs/2411.01192)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.01192.png)

Vote: 3

Authors: Fakhraddin Alwajih, Gagan Bhatia, Abdellah El Mekki, El Moatez Billah Nagoudi, Muhammad Abdul-Mageed

- ***What's New***: Swan과 ArabicMTEB는 아랍어 중심의 다이얼로그 인식형, 다국어 및 다문화 임베딩 모델과 벤치마크를 제공합니다. Swan은 ARBERTv2에 기반한 Swan-Small과 ArMistral에 기반한 Swan-Large 두 가지 모델로 구성되며, 아랍어 텍스트 임베딩을 위한 포괄적인 평가 벤치마크인 ArabicMTEB를 도입하여 다양한 다중 언어, 다지역, 다중 도메인, 다문화 성능을 평가합니다.
- ***Technical Details***: Swan 모델은 ARBERTv2와 추가 학습된 아랍어 대규모 언어 모델 ArMistral을 기반으로 합니다. 데이터 전처리 과정에서는 사람에 의해 생성된 데이터와 합성된 데이터를 사용하여 호환성을 높이기 위한 강화 학습을 거칩니다. ArabicMTEB는 8개의 다양한 태스크와 94개의 데이터세트를 포함하여 아랍어 텍스트 임베딩 능력을 전반적으로 평가하도록 설계되었습니다.
- ***Performance Highlights***: Swan-Large는 대부분의 아랍어 작업에서 Multilingual-E5-large를 능가하는 최신의 텍스트 임베딩 성능을 보여주었으며, Swan-Small도 Multilingual-E5-base를 일관되게 뛰어넘었습니다. 두 모델 모두 비용 효율성이 뛰어나고 문체와 문화를 인지할 수 있는 능력이 뛰어나다는 점에서 이점을 제공하며, 실제 응용 프로그램에서 높은 성능을 보여줍니다.

### [DimensionX: Create Any 3D and 4D Scenes from a Single Image with Controllable Video Diffusion](https://arxiv.org/abs/2411.04928)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.04928.png)

Vote: 16

Authors: Wenqiang Sun, Yueqi Duan, Jun Zhang, Fangfu Liu, Yikai Wang, Zilong Chen, Shuo Chen

- ***What's New***: DimensionX는 단일 이미지에서 제어 가능한 비디오 확산을 통해 사실적인 3D 및 4D 장면을 생성하는 혁신적인 프레임워크입니다. 이를 통해 3D 장면의 공간적 구조와 4D 장면의 시간적 진화를 비디오 프레임 시퀀스로 효과적으로 표현할 수 있습니다. DimensionX는 ST-Director를 사용하여 공간 및 시간 요소를 분리하고, 더 나아가 비디오 확산과 실제 세계 장면 간의 차이를 줄이기 위해 3D 생성에 대한 궤적 인식 메커니즘과 4D 생성에 대한 신원 보존 비소거 전략을 도입합니다.
- ***Technical Details***: ST-Director는 비디오 확산 모델에서 차원 인식 LoRA를 학습하여 공간 및 시간적 사전 요소를 구성하는 방식으로 공간 및 시간 요소를 분리합니다. 이 접근은 프레임 시퀀스에서의 공간 및 시간 변이 프레임을 생성하여, 3D 외형과 4D 동적 동작의 복원을 가능하게 합니다. 또한, 3D 장면 생성을 위한 궤적 인식 메커니즘과 4D 장면 생성을 위한 신원 보존 비소거 메커니즘을 설계하여 더 높은 현실적이고 제어 가능한 장면 합성을 가능하게 합니다.
- ***Performance Highlights***: DimensionX는 다양한 실제 및 합성 데이터셋에서 확장된 실험을 통해 제어 가능한 비디오 생성뿐만 아니라 3D 및 4D 장면 생성에서 이전 방법들보다 우수한 성능을 입증합니다. 이는 사실적이고 역동적인 환경을 생성하는 데 있어서 비디오 확산 모델이 제공하는 유망한 방향을 제시합니다.

### [SVDQunat: Absorbing Outliers by Low-Rank Components for 4-Bit Diffusion Models](https://arxiv.org/abs/2411.05007)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.05007.png)

Vote: 7

Authors: Junxian Guo, Yujun Lin, Zhekai Zhang, Jun-Yan Zhu, Tianle Cai, Chenlin Meng, Xiuyu Li, Enze Xie, Song Han, Muyang Li

- ***What's New***: SVDQuant는 대규모 확산 모델(Diffusion Models)의 가중치와 활성화를 4비트로 양자화(quantization)하면서 비정상 값을 낮은 계수(low-rank) 성분으로 흡수하여 발생할 수 있는 품질 저하를 최소화하는 새로운 접근 방식입니다. 이 방법론은 특히 16비트 모델의 성능을 유지하면서도 메모리 사용량을 3.5배, 처리 속도를 3배 가속할 수 있습니다.
- ***Technical Details***: SVDQuant는 초기 활성화(activation)에서 가중치(weight)로 비정상 값을 이동시키고, 고정밀(low-rank branch)의 Singular Value Decomposition (SVD)를 통해 이 가중치의 비정상 값을 흡수합니다. 이를 통해 양자화 시 발생하는 오류를 최소화합니다. 이 과정에서, 효율적인 추론 엔진(Nunchaku)을 설계하여 메모리 접근을 줄이고 고랭크 및 저비트 분기(kernel fusion)를 결합합니다.
- ***Performance Highlights***: SVDQuant는 FLUX.1 모델의 메모리 사용량을 최대 3.5배 줄이고, 16GB 랩탑 RTX4090 GPU에서는 NF4 표준보다 3배 빠른 속도를 보여주며, CPU 오프로딩을 제거하여 전체 처리 시간을 10.1배 단축시켰습니다. 또 다른 PIXART-Σ 모델에서는 원본 모델보다 높은 시각적 품질을 유지했습니다.

### [VideoGLaMM: A Large Multimodal Model for Pixel-Level Visual Grounding in Videos](https://arxiv.org/abs/2411.04923)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.04923.png)

Vote: 8

Authors: Fahad Shahbaz Khan, Eric Xing, Wenqi Zhu, Jiale Cao, Hanan Gani, Salman Khan, Shehan Munasinghe

- ***What's New***: VideoGLaMM은 비디오의 픽셀 수준의 시공간적 시각적 제공을 위한 다중 모달 모델로, 사용자 제공 텍스트 입력에 기반한 정밀한 시각적 제공 기능을 갖춘 최초의 모델입니다. 이 모델은 다층 언어 모델(Large Language Model; LLM), 2중 비전 인코더(dual vision encoder), 시공간 디코더(spatio-temporal decoder)가 통합되어 정밀한 시공간적 마스크 생성(mask generation)을 수행합니다.
- ***Technical Details***: VideoGLaMM는 LLM과, 공간적 및 시간적 특징을 동시에 추출하는 2중 비전 인코더, 픽셀 해상도의 시각적 출력을 위한 스페이셔-템포렐 픽셀 디코더(spatio-temporal pixel decoder)로 구성됩니다. 각 구성 요소는 V→L 및 L→V 어댑터(adapter) 통해 조정되어 비전-언어 정렬(Vision-Language alignment)을 촉진합니다. 본 벤치마크 데이터셋은 반자동 주석 파이프라인을 통해 수집된 38,000개의 비디오-QA 삼중 및 83,000개의 객체와 671,000개의 마스크를 포함합니다.
- ***Performance Highlights***: VideoGLaMM는 기본적인 비디오 대화 뿐만 아니라 더 복잡한 시각적 기반 대화 생성, 시각적 그라운딩, 비디오 구획 추천 등 여러 작업에서 기존 모델을 능가하는 성능을 나타냅니다. 여러 작업에서 Zero-shot 조건에서 최고의 성능을 발휘하며 높은 mIoU와 Recall 값을 기록하였습니다.

### [Inference Optimal VLMs Need Only One Visual Token but Larger Models](https://arxiv.org/abs/2411.03312)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.03312.png)

Vote: 5

Authors: J. Zico Kolter, Sachin Goyal, Kevin Y. Li, Joao D. Semedo

- ***What's New***: 이 연구는 Vision Language Models (VLMs)에서 추론 비용을 최적화하기 위한 새로운 스케일링 법칙을 제안합니다. 특히, 최소한의 시각적 토큰(Visual Tokens)을 사용하면서도 가능한 가장 큰 LLM을 사용해야 하는 추론 최적화 상태를 발견하였습니다. 이는 고도의 토큰 압축 설정을 위한 기존 접근 방식의 한계를 넘어서서 더 높은 압축 비율을 달성해야 함을 시사합니다.
- ***Technical Details***: 연구는 LLM 크기와 시각적 토큰 수의 상관관계를 모델링하는 스케일링 법칙을 개발하였습니다. 이 법칙은 시각적 토큰을 하나로 줄이고도, 가장 큰 LLM을 사용하는 것이 시각적 추론 작업에서 최소 다운스트림 오류를 발생시킨다는 것을 보여줍니다. 또한, 퀘리 기반의 토큰 압축(Query-Based Token Compression)을 도입하여 사용자 입력에 따라 중요한 정보를 유지하는 새로운 방법을 제안합니다.
- ***Performance Highlights***: 새로운 스케일링 법칙을 통해, 특정 추론 예산 내에서 가장 적합한 LLM을 선택하고 시각적 입력 토큰을 줄임으로써 성능을 향상시킬 수 있었으며, 수백의 토큰을 처리하는 대신 하나로 줄여도 금전적으로 최적의 추론 체제를 제공할 수 있음을 보여줍니다. 특히, 시각적 추론 작업에서 성능 저하가 거의 없는 점이 강조됩니다.

### [GazeGen: Gaze-Driven User Interaction for Visual Content Generation](https://arxiv.org/abs/2411.04335)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.04335.png)

Vote: 5

Authors: Wei-Te Mark Ting, Barbara De Salvo, Kao-Den Chang, H. T. Kung, He-Yen Hsieh, Ziyun Li, Sai Qian Zhang, Chiao Liu

- ***What's New***: GazeGen은 사용자의 눈동자 움직임을 사용하여 직관적인 시각 콘텐츠 생성 및 편집이 가능한 혁신적인 시스템입니다. 시선을 통해 관심 영역을 지정하여, 시각 콘텐츠를 손쉽게 조작할 수 있는 인터페이스를 제공하며, 이러한 '시선 기반 시각 콘텐츠 생성(Gaze-Driven Visual Content Generation)' 기능은 GazeGen이 최초로 제안한 것입니다.
- ***Technical Details***: GazeGen의 핵심은 DFT Gaze(DFT Gaze) 에이전트입니다. 이 모델은 경량화된 '실시간 시선 예측 모델(Real-Time Gaze Estimation Model)'로, 281K의 파라미터를 가지며 작은 '엣지 장치(Edge Device)'에서도 높은 정밀도의 예측을 구현합니다. '지식 증류(Knowledge Distillation)'와 '개인화 적응(Personal Adaptation)' 기술을 활용하여 효율성을 높였습니다. 시선 기반으로 다양한 객체를 감지 및 생성하는 데 그 활용 범위가 넓습니다.
- ***Performance Highlights***: DFT Gaze는 AEA와 OpenEDS2020 벤치마크에서 낮은 각도 시선 오차와 '낮은 지연율(Low Latency)'을 달성하여 엣지 디바이스인 '라즈베리 파이 4(Raspberry Pi 4)'에서 효과적으로 작동합니다. 학생 모델로서 ConvNeXt V2-A 보다 2배 빠르게 작동하며, 성능 저하를 최소화하면서도 높은 수준의 시선 추정 정확성을 유지합니다.

### [DynaMem: Online Dynamic Spatio-Semantic Memory for Open World Mobile Manipulation](https://arxiv.org/abs/2411.04999)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.04999.png)

Vote: 7

Authors: Zhanqiu Guo, Lerrel Pinto, Peiqi Liu, Nur Muhammad Mahi Shafiullah, Mohit Warke, Soumith Chintala, Chris Paxton

- ***What's New***: DynaMem은 변화하는 환경에서도 모바일 로봇의 제어를 위한 새로운 동적 공간-시맨틱 메모리(Dynamic Spatio-Semantic Memory) 시스템입니다. 로봇이 새로운 환경에서 탐색하고 객체를 탐색하며, 변화가 발생할 때마다 메모리를 지속적으로 업데이트할 수 있도록 설계되었습니다. 이는 기존의 정적 환경을 가정한 시스템보다 2배 이상의 성능 향상을 보여줍니다.
- ***Technical Details***: DynaMem은 3D 데이터 구조를 활용하여 환경의 동적 점 구름(Point Cloud)을 유지하며, VLM(Vision-Language Model)과 같은 최첨단 모델을 활용한 개방형 어휘 탐색이 가능합니다. 메모리는 포인트 클라우드를 Voxel화하여 표현하고, 환경의 변화를 실시간으로 관찰하고, 새로운 정보를 추가하거나 제거할 수 있도록 한다. 자연어로 쿼리된 객체를 찾기 위해 최신의 이미지와 연관된 Voxel을 이용합니다. VoxelMap은 최대 3개의 최적 이미지를 선택하여, mLLM(Multimodal Large Language Model)로 전달하여 쿼리를 수행합니다.
- ***Performance Highlights***: DynaMem은 세 개의 실제 환경에서 테스트되었으며, 전체 성공률 70%를 기록하여, 정적 시스템의 30%에 비해 상당한 성능 향상을 달성했습니다. 특히 변화하는 환경에서 동적 객체에 대한 적응력이 뛰어났으며, 이런 개선점은 다양한 응용 가능성을 엿볼 수 있는 결과였습니다.

### [Sample-Efficient Alignment for LLMs](https://arxiv.org/abs/2411.01493)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.01493.png)

Vote: 10

Authors: Changyu Chen, Zichen Liu, Chao Du, Min Lin, Wee Sun Lee

- ***What's New***: 이 논문은 대형 언어 모델(LLM)의 효율적 정렬을 위한 새로운 방법을 제안합니다. SEA(Sample-Efficient Alignment)는 인간의 선호에 맞춰 모델을 학습시키기 위해 매우 샘플 효율적인 알고리즘을 제공합니다. 이 알고리즘은 톰슨 샘플링(Thompson Sampling)을 기반으로 하며, 두 가지 다른 정렬 시나리오에서 응용될 수 있습니다.
- ***Technical Details***: SEA 알고리즘은 톰슨 샘플링(Thompson Sampling)에 기반하여 컨텍스트 결투 밴딧(Contextual Dueling Bandits) 문제를 해결합니다. 이 알고리즘은 온라인 상호작용(online interaction)과 능동 탐색(active exploration)이라는 두 가지 주요 특성을 만족합니다. SEA는 딥 앙상블(Deep Ensemble) 접근법을 사용하여 보상 모델의 불확실성을 포착하고, 이를 통해 샘플 효율성을 높입니다. 응답 선택 과정은 정책 기반 탐색(policy-guided search)을 통해 가장 유용한 응답을 생성하게 됩니다.
- ***Performance Highlights***: SEA는 다양한 모델 규모(1B, 2.8B, 6.9B)와 선호 학습 알고리즘(DPO, IPO, SLiC)에서 상당한 성능 향상을 보여줍니다. 오픈소스인 코드베이스와 함께 제공되는 SEA는 최종 성능에서 눈에 띄는 개선을 제공하며, 샘플 효율성 면에서 다른 최근의 탐색 방법들을 능가합니다. 특히, SEA는 XPO, APL과 같은 다른 탐색 방법과 비교하여 2-5배 더 나은 샘플 효율성을 달성합니다.

### [GarVerseLOD: High-Fidelity 3D Garment Reconstruction from a Single In-the-Wild Image using a Dataset with Levels of Details](https://arxiv.org/abs/2411.03047)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.03047.png)

Vote: 6

Authors: Zirong Jin, Wanghao Du, Xiaoguang Han, Weikai Chen, Zhongjin Luo, Haolin Liu, Wanhu Sun, Chenghong Li, Yinyu Nie

- ***What's New***: 이 논문에서는 GarVerseLOD라는 새로운 데이터셋과 프레임워크를 소개합니다. 이는 야생 환경(single in-the-wild image)에서 단일 이미지로부터 고품질의 독립적인 3D 의류 재구성을 가능하게 합니다. 이로써 복잡한 의상 변형과 본 자세에 영향을 받지 않는 특별한 견고성을 제공합니다.
- ***Technical Details***: GarVerseLOD는 레벨 오브 디테일(Levels of Details; LOD)을 활용하여 복잡한 의류 변형과 미세한 표면 디테일을 포함하는 6,000개의 고품질 수작업 3D 의류 메쉬를 수집합니다. 각 모델은 세 가지 기본 데이터베이스로 분류되어 있습니다: 간단한 'T자형 포즈' 의상, 간단한 디테일 없이 'T자형 포즈' 모델과 세밀한 로컬 기하학적 디테일을 포함하는 모델 페어, 자세 섞임을 통한 전역 변형을 포함한 의류 변형 데이터베이스. 이러한 계층적인 데이터셋은 추정 과정을 더 쉽게 하고 일반화 능력과 추론 정확도를 높이는 데 기여합니다.
- ***Performance Highlights***: 실험 결과에 따르면 GarVerseLOD는 이전 방법들에 비해 다양한 포즈, 조명, 폐색, 변형에 대해 일관성이 높고 우수한 품질의 독립적인 의류 조각을 생성할 수 있음을 보여주었습니다. 특히, 최첨단 방법보다 향상된 일반화 능력을 입증하여, 상용 및 오픈 소스 작업 간의 경쟁력을 드러냈습니다.

### [Multi-expert Prompting Improves Reliability, Safety, and Usefulness of Large Language Models](https://arxiv.org/abs/2411.00492)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.00492.png)

Vote: 5

Authors: Duong Ngoc Yen, Kenji Kawaguchi, Do Xuan Long, Nancy F. Chen, Anh Tuan Luu, Min-Yen Kan

- ***What's New***: Multi-expert Prompting은 다양한 '전문가' 역할을 시뮬레이션하면서 LLM(Large Language Model)이 주어진 입력 지침을 이행하도록 유도하는 새로운 접근 방식입니다. 여러 전문가의 답변을 집계하고, 이를 통합하여 최적의 답변을 선택합니다. 이를 통해 생성 모델의 진실성(truthfulness), 사실성(factuality), 정보 제공 능력(informativeness), 유용성(usefulness)을 향상시키며, 독성을 줄이고, 해악성도 감소시킵니다.
- ***Technical Details***: Multi-expert Prompting은 명사그룹기법(Nominal Group Technique)을 활용하여, 일곱 가지 잘 설계된 하위 작업을 통해 다양한 전문가의 시각을 포함하는 다면적 답변을 도출합니다. 첫째, LLM이 제로샷(zero-shot) 프롬프트 방식을 통해 n개의 전문가 역할을 생성하고, 각각의 역할로 주어진 지침에 대해 독립적으로 답변을 생성합니다. 이어서 개별 답변과 통합된 답변을 평가하여 최적의 답변을 선택합니다.
- ***Performance Highlights***: Multi-expert Prompting은 ChatGPT와 같은 강력한 LLM에서 진실성과 사실성에서 현저한 성능 향상을 기록했습니다. 또한, 진실성을 개선하여 현재의 세가지 선택 중 최고 성능을 달성하였습니다. 이는 다양한 전문가의 관점을 통합하여 결론을 도출하는 민주적인 접근이 진실성을 높이는 데 기여했음을 시사합니다.

### [Survey of Cultural Awareness in Language Models: Text and Beyond](https://arxiv.org/abs/2411.00860)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.00860.png)

Vote: 23

Authors: Jiho Jin, Junyeong Park, Srishti Yadav, Arnav Arora, Faiz Ghifari Haznitrama, Inhwa Song, Junho Myung, Alice Oh, Siddhesh Pawar, Isabelle Augenstein

- ***What's New***: 이 논문은 연구자들이 텍스트 기반 및 멀티모달 언어 모델(LLM)의 문화적 포용성 및 인식을 높이기 위해 수행하는 노력을 조사합니다. 특히 심리학 및 인류학에서 유래한 문화 정의를 통해 LLM에서의 문화 인식 정의를 시작으로 다양한 문화적 데이터셋 생성 및 평가 방법론을 분석합니다.
- ***Technical Details***: 이 논문은 LLM의 문화적 인식 벤치마크(benchmark) 및 데이터셋을 만들기 위한 다양한 방법론을 다룹니다. 우선, 문화적 포용성을 위해 크로스-컬처럴 데이터셋을 제작하는 방법론을 조사하며, 이는 예를 들어 웹 크롤링이나 인간 전문가의 참여를 통해 이루어집니다. 이와 함께, LLM을 문화적으로 조율하기 위한 다양한 모델 학습 및 프롬프트 기반 접근법을 살펴봅니다.
- ***Performance Highlights***: 일부 독점 대형 언어 모델들은 문화적 인식과 관련된 다양한 영역에서 뛰어난 성능을 보여줍니다. 그러나 아직은 불완전하며, 특히 비서구적 관점에 대한 성능이 부족하다는 결과가 나오고 있습니다. 이는 후속 연구가 LLM의 크로스-컬쳐럴한 이해를 강화하는데 초점을 맞춰야 함을 시사합니다.

### [Controlling Language and Diffusion Models by Transporting Activations](https://arxiv.org/abs/2410.23054)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2410.23054.png)

Vote: 14

Authors: Arno Blaas, Pau Rodriguez, Michal Klein, Luca Zappella, Marco Cuturi, Nicholas Apostoloff, Xavier Suau

- ***What's New***: Activation Transport (ACT)는 최적 운송 이론(Optimal Transport Theory)으로 모델의 활성화를 조정하는 일반 프레임워크입니다. 이는 기존의 여러 활성화 조정 방법들을 일반화했고, 여러 모달리티(Modality)에 걸쳐 모델 행동을 미세하게 제어할 수 있습니다.
- ***Technical Details***: ACT는 모듈에 구애받지 않으며, 최적 운송 지도하에 활성화 지도(Transport)를 수행합니다. Linear-ACT는 독립적인 단항 변환 지도 패밀리를 활용하여 훈련된 샘플을 통해 활성화에서 목표 분포로의 선형 변환을 적용합니다. 이는 제로 오버헤드로 내부 활성화 분포를 보존하여 제어를 가능하게 합니다. 또한 조절 매개변수 λ를 통해 0에서 1 사이에서 제어 강도를 설정할 수 있습니다.
- ***Performance Highlights***: Linear-ACT는 독성 저감, 개념 유도 및 진실성 향상 작업에서 기존 방법과 동등하거나 더 나은 성능을 보여주었습니다. 시각적 확산 모델에 있어서도 STYLX 및 FLUX와 같은 모델에서 세밀한 스타일 제어와 개념 제거에 효과적입니다. 연구는 다른 모달리티와 접근법에서 일관된 결과를 제공합니다.

### [AutoVFX: Physically Realistic Video Editing from Natural Language Instructions](https://arxiv.org/abs/2411.02394)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.02394.png)

Vote: 13

Authors: Hao-Yu Hsu, Zhi-Hao Lin, Hongchi Xia, Albert Zhai, Shenlong Wang

- ***What's New***: AutoVFX는 자연어 지시를 활용하여 단일 비디오에서 사실적이고 동적인 VFX 동영상을 자동으로 생성하는 프레임워크입니다. 이 시스템은 신경 장면 모델링, 대형 언어 모델(LLM) 기반의 코드 생성, 그리고 물리 시뮬레이션을 통합하여 물리적으로 타당하며 현실감 있는 편집 효과를 제공합니다.
- ***Technical Details***: AutoVFX의 핵심은 신경 장면 모델링과 LLM 기반의 코드 생성, 물리 시뮬레이션의 혁신적인 통합입니다. 3D 장면 모델링(3D Scene Modeling) 모듈은 장면의 기하학, 외관, 의미를 코드화하여 다양한 시뮬레이션과 렌더링 작업을 가능하게 합니다. 장면 편집 및 시뮬레이션(Editing and Simulation)은 Blender와 같은 물리 기반 시뮬레이션 엔진을 활용하여 실행되며, 자연어 지침을 받아 LLM을 통해 편집 프로그램을 생성합니다.
- ***Performance Highlights***: AutoVFX는 다양한 비디오 및 지침에 대한 실험을 통해 다른 경쟁 방법에 비해 생성 품질, 지침 정렬성, 편집 다변성 및 물리적 타당성 측면에서 월등한 성능을 보였습니다. 이러한 결과는 AutoVFX의 접근법이 얼마나 효과적이며 편리한지를 입증하며, VFX를 대중화할 수 있는 잠재력을 강조합니다.

### [IGOR: Image-GOal Representations are the Atomic Control Units for Foundation Models in Embodied AI](https://arxiv.org/abs/2411.00785)

![](https://cdn-thumbnails.huggingface.co/social-thumbnails/papers/2411.00785.png)

Vote: 8

Authors: Junliang Guo, Jiang Bian, Pushi Zhang, Chuheng Zhang, Li Zhao, Tianyu He, Derek Cathera Yang, Xiaoyu Chen

- ***What's New***: Image-GOal Representations (IGOR)는 인간과 다양한 로봇들 간의 통합적이고 의미 일관적인 행동 공간을 학습하는 새로운 방식이며, 이는 대규모 인간 및 로봇 활동 데이터 간의 지식 이전을 가능하게 합니다. 이를 통해 IGOR는 인터넷 규모의 비디오 데이터에 잠재 행동 레이블을 생성하여, 로봇과 인간이 수행하는 다양한 작업에 대한 정책 및 세계 모델을 훈련할 수 있습니다. IGOR는 사용자와 로봇 간의 지식 이전과 제어의 새로운 가능성을 열어줍니다.
- ***Technical Details***: IGOR는 비디오의 초깃 상태와 목표 상태 간의 시각적 변화를 잠재 행동으로 압축하여 인간과 로봇 간의 다양한 구현을 아우르는 통합 잠재 행동 공간을 학습합니다. 이 모델은 Vision Transformer(ViT) 및 Spatio-Temporal Transformer(ST-transformer)를 사용하여 시각적 변화를 학습하고, Rectified Flow를 활용해 비디오 데이터를 통해 미래 프레임을 예측합니다. 또다른 핵심 요소로서, Foundation Policy 모델과 세계 모델이 잠재 행동을 사용하여 작업을 수행합니다.
- ***Performance Highlights***: IGOR는 RT-1 데이터셋에 대해 OOD (out-of-distribution) 평가를 실시하였으며, 비슷한 잠재 행동을 가진 이미지 쌍들이 유사한 시각적 변화를 보이는 것을 확인했습니다. 또한, 인간 행동 비디오에서 추출한 잠재 행동을 로봇 영상에 적용하여 로봇이 인간 행동을 모방할 수 있음을 입증했습니다. 이는 소량의 데이터로도 로봇의 작업 성능을 향상시킬 수 있는 가능성을 보여줍니다.

## License

This project is licensed under the [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/deed.ko) license.

## Citation

If this work is helpful, please kindly cite as:

```bibtex
@misc{daily_papers,
  title = {Huggingface Daily Papers},
  author = {AK391},
  howpublished = {\url{https://huggingface.co/papers}},
  year = {2023}
}

@misc{daily_papers_ko,
  title = {Automatically translate and summarize huggingface's daily papers into korean},
  author = {l-yohai},
  howpublished = {\url{https://github.com/l-yohai/daily_papers_ko}},
  year = {2023}
}
```

## Star History

![Star History Chart](https://api.star-history.com/svg?repos=l-yohai/daily_papers_ko&type=Date)
