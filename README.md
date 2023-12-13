# Daily Papers

## Project Description

This project aims to automatically translate and summarize [Huggingface's daily papers](https://huggingface.co/papers) into Korean using ChatGPT.

Thanks to [@AK391](https://github.com/AK391) for great work.


## Daily Papers (2023-12-13)

### [DiffMorpher: Unleashing the Capability of Diffusion Models for Image Morphing](https://arxiv.org/abs/2312.07409)

[Watch Video](https://cdn-uploads.huggingface.co/production/uploads/60f1abe7544c2adfd699860c/pPBftW9u_SvGH1HLzFDu-.mp4)
<div><video controls src="https://cdn-uploads.huggingface.co/production/uploads/60f1abe7544c2adfd699860c/pPBftW9u_SvGH1HLzFDu-.mp4" muted="false"></video></div>

Vote: 2

Authors: Kaiwen Zhang, Yifan Zhou, Xudong Xu, Xingang Pan, Bo Dai

- 확산 모델이 이전의 생성 모델들을 능가하는 뛰어난 이미지 생성 품질을 달성했지만, 구조화되지 않은 잠재 공간 때문에 두 이미지 샘플 사이의 부드러운 보간을 수행하기 어렵다는 한계가 있었습니다.
- 이 연구에서는 DiffMorpher라는 첫 번째 접근 방식을 제시하여 확산 모델을 사용하여 자연스럽고 부드러운 이미지 보간을 가능하게 합니다.
- DiffMorpher의 핵심 아이디어는 두 이미지의 의미를 LoRAs로 각각 적용하고 LoRA 매개변수와 잠재 잡음을 보간하여 의미가 부드럽게 전환되도록 하는 것입니다.
- 주목할 만한 것은, 이 방식은 주석 없이도 자동적으로 상응하는 이미지를 생성할 수 있습니다.
- 또한, 연속되는 이미지 사이의 부드러움을 더욱 강화하기 위해 주의력 보간 및 주입 기술과 새로운 샘플링 일정을 제안합니다.
- 광범위한 실험을 통해, DiffMorpher가 다양한 대상 카테고리에서 예전 방법들보다 훨씬 더 나은 이미지 형태 변환 효과를 달성하며, 확산 모델과 GAN의 주요 기능적 차이점을 다리를 놓는 데 성공했습니다.

### [Fast Training of Diffusion Transformer with Extreme Masking for 3D Point Clouds Generation](https://arxiv.org/abs/2312.07231)

![](https://cdn-uploads.huggingface.co/production/uploads/60f1abe7544c2adfd699860c/0X51hP2vD0fcaE1QkLXkC.png)

Vote: 1

Authors: Shentong Mo, Enze Xie, Yue Wu, Junsong Chen, Matthias Nießner, Zhenguo Li

- 최근에는 3D 포인트 클라우드 생성을 위해 효과적인 것으로 알려진 확산 변환기(Diffusion Transformers)가 있지만 고해상도 3D 복셀에 대한 훈련은 복셀의 추가 차원에서 오는 어텐션 연산자의 입방 복잡성 때문에 비현실적으로 비쌉니다.
- FastDiT-3D라는 새롭고 혁신적인 마스크 확산 변환기를 제안하여 효율적으로 3D 포인트 클라우드 생성을 위한 훈련 비용을 크게 줄입니다.
- 마스크된 자동인코더에서 영감을 받아 동적으로 노이즈 제거 과정을 마스크된 복셀화 포인트 클라우드에서 운영합니다.
- 또한 복셀화된 포인트 클라우드에서 배경/전경 정보를 적응적으로 집계하기 위한 새로운 복셀 인식 마스킹 전략을 제안합니다.
- 극단적인 마스킹 비율인 거의 99%로 최첨단 성능을 달성합니다.
- 다중 카테고리 3D 생성을 개선하기 위해 각 카테고리가 다른 전문가들과 다른 확산 경로를 배울 수 있도록 3D 확산 모델에서 전문가 혼합(Mixture-of-Expert, MoE)을 도입합니다.
- ShapeNet 데이터셋에 대한 실험 결과는 고해상도 및 다양성있는 3D 포인트 클라우드 생성에서 최첨단 성능을 달성함을 보여줍니다.
- FastDiT-3D는 원래 훈련 비용의 단 6.5%를 사용하여 128 해상도 복셀 포인트 클라우드를 생성할 때 1-Nearest Neighbor 정확도와 커버리지 메트릭을 개선합니다.

### [Rethinking Compression: Reduced Order Modelling of Latent Features in Large Language Models](https://arxiv.org/abs/2312.07046)

![](https://cdn-uploads.huggingface.co/production/uploads/60f1abe7544c2adfd699860c/sqzUUhXvvM9ZIuL_mmT7v.png)

Vote: 1

Authors: Arnav Chavan, Nahush Lele, Deepak Gupta

- 대규모 언어 모델(Large Language Models, LLMs)의 막대한 규모로 인해 기존의 압축 방법론을 직접 적용하기가 비현실적이라는 문제를 지적합니다.
- 기존의 최소한의 기울기(gradient) 업데이트조차도 소비자급 하드웨어에서는 높은 계산 요구로 도전이 됩니다.
- 특히 이 연구는 피쳐 공간 내의 저차원 분해(low-rank decomposition) 및 가중치 공간의 재매개변수화(re-parameterization)에 기반한 대규모 언어 모델의 파라메트릭하고 실용적인 압축 방법을 소개합니다.
- 이 압축 기술은 레이어별로 작동하여 GPU 장치가 필요 없으며, 메모리와 시간의 엄격한 제약 조건 내에서 십억 규모의 모델을 압축할 수 있도록 합니다.
- 메트릭스 분해를 활용하여 현존하는 최고의 구조화된 가지치기(structured pruning) 방법보다 우수한 효과를 입증하는 모델 압축 분야에서의 중요한 진전을 나타냅니다.

### [Alignment for Honesty](https://arxiv.org/abs/2312.07000)

![](https://cdn-uploads.huggingface.co/production/uploads/60f1abe7544c2adfd699860c/9hBz8whuve-tqFEH6Gh1X.png)

Vote: 1

Authors: Yuqing Yang, Ethan Chern, Xipeng Qiu, Graham Neubig, Pengfei Liu

- 최근 연구가 사람들의 의도에 맞게 대규모 언어 모델(LLM)의 유용성과 무해함을 향상시키기 위한 알라인먼트 기법을 적용하는 데 중요한 진전을 이루었습니다.
- 이 논문에서는 LLM이 지식이 부족할 때 적극적으로 답변을 거부하도록 하면서도 지나치게 보수적이지 않는 '정직성에 대한 알라인먼트'의 중요성을 주장합니다.
- LLM의 지식 한계를 파악하는 것은 복잡한 과제이며, 이는 지표 개발, 벤치마크 생성, 훈련 방법론 측면에서 종합적인 해결책을 요구합니다.
- 저자들은 공자의 『논어』에서 영감을 받아 정직성을 정의하고 정확한 문제 정의를 수립하여 이 문제에 접근합니다.
- 또한, LLM의 정직성을 정량화하고 정렬 후 진전을 측정하는 데 효과적인 지표를 개발합니다.
- 이 연구는 다른 작업에서의 성능을 희생하지 않으면서 정직성을 강화하는 몇 가지 효율적인 미세 조정 기법을 도입한 유연한 훈련 프레임워크를 소개합니다.
- 광범위한 실험을 통해 이러한 조정된 모델이 제안된 지표에 따라 정직성이 크게 향상됨을 확인합니다.
- 연구의 진전을 촉진하기 위해 https://github.com/GAIR-NLP/alignment-for-honesty 에서 정직성에 맞춰진 모델, 정직성 알라인먼트를 위한 훈련 및 평가 데이터셋, 개념 용어집, 관련 소스 코드 등을 오픈 소스로 제공합니다.

### [COLMAP-Free 3D Gaussian Splatting](https://arxiv.org/abs/2312.07504)

![](https://cdn-uploads.huggingface.co/production/uploads/60f1abe7544c2adfd699860c/DV8LfQsmYeC8g09vzSg5U.png)

Vote: -

Authors: Yang Fu, Sifei Liu, Amey Kulkarni, Jan Kautz, Alexei A. Efros, Xiaolong Wang

- 신경 렌더링은 장면 재구성과 새로운 시점 합성 분야에서 인상적인 발전을 이룩했으나, 정확히 사전 계산된 카메라 포즈에 크게 의존한다.
- 사전 처리된 카메라 포즈 없이 신경 복사장(NeRFs)을 훈련시키기 위한 여러 노력에도 불구하고, NeRFs의 내재적 표현은 3D 구조와 카메라 포즈를 동시에 최적화하는 추가적인 도전을 제공한다.
- 반면에 최근에 제안된 3D 가우스 스플래팅은 명시적인 포인트 클라우드 표현을 제공함으로써 새로운 기회를 제공한다.
- 본 논문은 입력된 비디오 스트림의 연속성과 명시적인 기하학적 표현을 활용하여, 구조적인 모양 추적(SfM) 전처리 없이 새로운 시점 합성을 수행한다.
- 입력 프레임을 순차적으로 처리하며 한 번에 하나의 입력 프레임을 취해 3D 가우스 세트를 점진적으로 성장시키며, 카메라 포즈를 사전에 계산할 필요가 없다.
- 제안된 방법은 대규모 모션 변경이 있는 시점 합성과 카메라 포즈 추정에서 이전 접근 방식들에 비해 크게 향상되었다.
- 프로젝트 페이지는 주소 [https://oasisyang.github.io/colmap-free-3dgs](https://oasisyang.github.io/colmap-free-3dgs)에서 확인할 수 있다.

### [How Well Does GPT-4V(ision) Adapt to Distribution Shifts? A Preliminary Investigation](https://arxiv.org/abs/2312.07424)

![](https://cdn-uploads.huggingface.co/production/uploads/60f1abe7544c2adfd699860c/6etjFARZEbazSch-T6SxA.png)

Vote: -

Authors: Zhongyi Han, Guanglin Zhou, Rundong He, Jindong Wang, Xing Xie, Tailin Wu, Yilong Yin, Salman Khan, Lina Yao, Tongliang Liu, Kun Zhang

- 기계 학습에서 훈련 시나리오와 다른 배포 조건 하에서의 일반화, 즉 분포 변화에 대한 적응은 기후 모델링, 생물의학, 자율 주행 등의 분야에서 매우 중요합니다.
- 대규모 사전 훈련과 작업 다양성으로 구별되는 기초 모델의 출현으로 인해 이러한 모델들의 분포 변화에 대한 적응 가능성에 대한 관심이 커졌습니다.
- GPT-4V(ision)는 이상 감지, 비디오 이해, 이미지 생성, 의료 진단 등 다양한 분야에서 폭넓게 적용되는 가장 발전된 공개적으로 이용 가능한 멀티모달 기초 모델로 활동하고 있습니다.
- 그러나 GPT-4V의 데이터 분포에 대한 강인함은 대체로 탐색되지 않았습니다.
- 이 연구는 GPT-4V의 적응 및 일반화 능력을 엄격하게 평가하여 CLIP 및 LLaVA와 같은 주목할만한 모델들과 벤치마킹합니다.
- 저자들은 자연, 의료, 분자 분야를 아우르는 13개의 다양한 데이터셋을 통해 GPT-4V의 제로 샷 일반화 능력을 깊이있게 탐구합니다.
- 또한, 통제된 데이터 변형에 대한 적응성을 조사하고 인-콘텍스트 학습이 적응을 향상시키는 도구로서의 효과를 검토합니다.
- 연구 결과는 분포 이동에서 GPT-4V의 능력 경계를 설명하며 다양한 시나리오에서의 강점과 한계를 밝힙니다.
- 특히, 이 연구는 AI 기초 모델이 분포 변화에 얼마나 잘 일반화되는지에 대한 이해를 돕고, 그 적응성과 강인성에 대한 중요한 통찰을 제공합니다.
- 관련 코드는 https://github.com/jameszhou-gl/gpt-4v-distribution-shift 에서 공개적으로 이용 가능합니다.

### [FreeInit: Bridging Initialization Gap in Video Diffusion Models](https://arxiv.org/abs/2312.07537)

![](https://cdn-uploads.huggingface.co/production/uploads/60f1abe7544c2adfd699860c/UiQlReF6EXNfVLrI_8z2-.png)

Vote: -

Authors: Tianxing Wu, Chenyang Si, Yuming Jiang, Ziqi Huang, Ziwei Liu

- 비디오 생성을 위한 확산 모델의 추론 결과가 시간적 일관성과 자연스러운 역동성 측면에서 불만족스러운 문제점이 있음.
- 연구진은 비디오 확산 모델의 소음 초기화에 주목하여 훈련과 추론 간 암묵적인 간극이 있음을 발견하고, 이것이 추론 품질의 불만족을 초래함을 밝혀냄.
- 초기 잠재 변수의 공간적-시간적 주파수 분포가 추론 시 훈련 때와 다르며, 저주파 성분이 제거 과정에 중대한 영향을 미침을 주요 발견사항으로 확인.
- 이러한 관찰을 바탕으로, 연구진은 추론 샘플링 전략인 FreeInit을 제안하고, 이는 확산 모델에 의해 생성된 비디오의 시간적 일관성을 크게 향상시킴.
- 추론 동안 초기 잠재 변수의 공간적-시간적 저주파 성분을 반복적으로 정제하여 훈련과 추론 사이의 초기화 간극을 보상하는 방식으로 작용.
- FreeInit은 추가적인 훈련 없이도 다양한 텍스트-비디오 생성 모델의 결과를 일관성 있게 개선함을 광범위한 실험을 통해 입증.

### [PEEKABOO: Interactive Video Generation via Masked-Diffusion](https://arxiv.org/abs/2312.07509)

![](https://cdn-uploads.huggingface.co/production/uploads/60f1abe7544c2adfd699860c/BEB9BbR70W_YtxAyw6TvR.qt)

Vote: -

Authors: Yash Jain, Anshul Nasery, Vibhav Vineet, Harkirat Behl

- 최근 텍스트-비디오 생성 분야에서 고품질 실제적인 비디오를 생성하는 모델이 발전하였지만 사용자가 상호 작용하여 비디오를 제어하고 생성하는 기능은 부족합니다.
- 이 문제를 해결하기 위해, 우리는 분산 모델 기반 비디오 생성에 시공간적 제어를 가능하게 하는 새로운 공간-시간 마스크 주의 모듈인 Peekaboo를 제안합니다.
- Peekaboo 모듈은 교육이 필요 없고, 기존 비디오 생성 모델에 추가할 때 추론 오버헤드가 발생하지 않으며 시공간 제어를 가능하게 합니다.
- 또한, 상호 작용적 비디오 생성 작업을 평가하기 위한 벤치마크도 제시합니다.
- 질적 및 양적 평가를 통해, Peekaboo가 제어 비디오 생성을 가능하게 하며 기존 모델들을 대비하여 최대 3.8배의 mIoU 상승을 얻을 수 있음을 증명합니다.

### [VILA: On Pre-training for Visual Language Models](https://arxiv.org/abs/2312.07533)

![](https://cdn-uploads.huggingface.co/production/uploads/60f1abe7544c2adfd699860c/Yg0zBVAZpvV-jWC3DT13X.png)

Vote: -

Authors: Ji Lin, Hongxu Yin, Wei Ping, Yao Lu, Pavlo Molchanov, Andrew Tao, Huizi Mao, Jan Kautz, Mohammad Shoeybi, Song Han

- 이 연구에서는 대규모 언어 모델의 최근 성공에 따라 급속하게 진전된 시각 언어 모델(VLM)에 대한 시각적 명령어 튜닝의 확장을 시도했으며, 모델이 두 모달리티에서 합동 모델링을 수행하는 방법을 배우는 시각 언어의 사전 훈련 과정을 심층적으로 연구했다.
- 사전 훈련 동안 언어 모델을 고정하는 것은 일정 수준의 제로샷 성능을 낼 수 있지만, 맥락 내 학습 능력을 갖추기 위해서는 언어 모델의 고정 해제가 필요하다는 주요 결과를 발견했다.
- 본 논문은 상호 교차된 사전 훈련 데이터가 유리하며 이미지-텍스트 쌍만으로는 최적이 아니라는 점을 보여주었다.
- 이미지-텍스트 데이터에 텍스트 전용 지시 데이터를 다시 혼합하는 것은 텍스트 전용 작업의 저하를 해결할 뿐만 아니라 VLM 작업 정확도를 향상시킨다.
- 이 연구는 개선된 사전 훈련 레시피를 사용하여, 예를 들어 LLaVA-1.5와 같은 최신 모델을 주요 벤치마크에서 일관되게 능가하는 VILA라는 시각 언어 모델 패밀리를 구축했다.
- 멀티모달 사전 훈련은 VILA의 여러 매력적인 속성을 밝혀내는 데 도움이 되며, 이에는 다중 이미지 추론, 향상된 맥락 내 학습, 그리고 더 나은 세계 지식이 포함된다.

### ["I Want It That Way": Enabling Interactive Decision Support Using Large Language Models and Constraint Programming](https://arxiv.org/abs/2312.06908)

![](https://cdn-uploads.huggingface.co/production/uploads/60f1abe7544c2adfd699860c/taoZ0wjnCyOWlTnmM8mYU.png)

Vote: -

Authors: Connor Lawless, Jakob Schoeffer, Lindy Le, Kael Rowan, Shilad Sen, Cristina St. Hill, Jina Suh, Bahar Sarrafzadeh

- 사용자 기반을 정확하게 모델링하는 것은 의사결정 지원 시스템의 성공에 중요한 요소이며, 사용자는 종종 선호도를 추출하는 과정 중에 개발한다는 심리학 연구 결과를 바탕으로, 시스템-사용자 상호작용의 중요성을 강조한다.
- 본 논문에서는 대규모 언어 모델(Large Language Models, LLMs)과 제약 프로그래밍(Constraint Programming)을 결합하여 상호작용적 의사결정 지원을 용이하게 하는 새로운 접근 방식을 소개한다.
- 연구진은 회의 일정 조정이라는 시간 소모적인 일상 활동을 통해 이 혼합 프레임워크를 검토한다.
- 연구진은 새로운 프레임워크를 평가하기 위해 세 가지 연구를 수행했는데, 이에는 일기 연구(n=64)를 통한 문맥적 일정 선호도 특성을 분석하고, 시스템 성능의 양적 평가 및 프로토타입 시스템을 사용한 사용자 연구(n=10)가 포함된다.
- 이 작업은 반복적 선호도 추출을 위한 LLM과 최적화 접근법의 잠재력을 강조하고 인간-시스템 협동 의사결정 과정을 지원하는 시스템을 개발하기 위한 설계 고려 사항을 제시한다.

### [Honeybee: Locality-enhanced Projector for Multimodal LLM](https://arxiv.org/abs/2312.06742)

![](https://cdn-uploads.huggingface.co/production/uploads/60f1abe7544c2adfd699860c/9VVzgks022Bj6Iq8RTKpu.png)

Vote: -

Authors: Junbum Cha, Wooyoung Kang, Jonghwan Mun, Byungseok Roh

- 멀티모달 대형 언어 모델(MLLMs)에서 시각적 프로젝터는 사전 훈련된 비전 인코더를 LLMs과 연결하여 시각적 이해를 가능하게 하고 LLMs의 강인한 기능을 활용하는 중요한 역할을 합니다.
- 본 연구에서는 프로젝터의 두 가지 필수적인 특성을 확인하였는데, (i) MLLMs의 전체 효율성에 중요한 시각적 토큰 수를 관리할 수 있는 유연성, (ii) 공간적 이해에 필수적인 시각적 특징으로부터의 로컬 컨텍스트 보존입니다.
- 이러한 발견에 기반하여, 우리는 유연성과 지역성을 강화한 새로운 프로젝터 디자인을 제안하였으며, 이는 두 개의 바람직한 속성을 효과적으로 만족시킵니다.
- 또한, 다양하고 다면적인 지시 데이터셋을 효과적으로 활용하기 위한 종합적인 전략을 제시하였습니다.
- 광범위한 실험을 통해 개별 디자인 선택이 미치는 영향을 검토했으며, 제안된 MLLM인 Honeybee는 MME, MMBench, SEED-Bench, LLaVA-Bench 등 여러 벤치마크에서 이전의 최신 방법들을 뛰어넘는 성능을 보여주었습니다.
- Honeybee 모델은 효율성이 현저히 높아졌으며, 해당 코드와 모델들은 https://github.com/kakaobrain/honeybee 에서 제공됩니다.

### [Steering Llama 2 via Contrastive Activation Addition](https://arxiv.org/abs/2312.06681)

![](https://cdn-uploads.huggingface.co/production/uploads/60f1abe7544c2adfd699860c/TD3n0VQb1Cus5m8_0yFmX.png)

Vote: -

Authors: Nina Rimsky, Nick Gabrieli, Julian Schulz, Meg Tong, Evan Hubinger, Alexander Matt Turner

- 이 연구는 언어 모델을 제어하기 위한 새로운 방법인 Contrastive Activation Addition (CAA)를 제안합니다.
- CAA는 사실적인 대응과 환상적인 대응과 같이 원하는 행동의 긍정적 및 부정적 예시 쌍 사이의 잔차 스트림 활성화 차이를 평균하여 "제어 벡터"를 계산합니다.
- 추론 시, 이러한 제어 벡터는 사용자 프롬프트 뒤의 모든 토큰 위치에 긍정적 또는 부정적 계수로 추가되어 대상 행동의 정도를 정밀하게 제어할 수 있게 합니다.
- CAA의 효과는 다중 선택 행동 질문 데이터셋과 개방형 생성 과제를 사용하여 Llama 2 Chat에서 평가되었습니다.
- 결과적으로 CAA는 모델의 행동을 상당히 변화시켰으며, 전통적인 방법인 파인튜닝 및 소수샘플 프롬프팅보다 우수한 성능을 보였음을 입증했습니다.
- 또한, CAA는 모델의 능력을 최소한으로 감소시키면서 고차원 개념이 대규모 언어 모델(LLMs)에서 어떻게 표현되는지에 대한 통찰력을 제공하는 다양한 활성화 공간 해석 방법을 사용합니다.

### [Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations](https://arxiv.org/abs/2312.06674)

![](https://cdn-uploads.huggingface.co/production/uploads/60f1abe7544c2adfd699860c/nn0XgqkxcVD2HWh56_vWC.png)

Vote: -

Authors: Hakan Inan, Kartikeya Upasani, Jianfeng Chi, Rashi Rungta, Krithika Iyer, Yuning Mao, Michael Tontchev, Qing Hu, Brian Fuller, Davide Testuggine, Madian Khabsa

- 'Llama Guard'란 인간-AI 대화 사례에 특화된 LLM(대규모 언어 모델) 기반의 입력-출력 보호 모델을 소개합니다.
- 이 모델은 LLM 프롬프트에서 발견되는 특정한 안전 위험 분류를 가능하게 하는 안전 위험 분류 체계(taxonomy)를 포함합니다.
- 이 분류 체계는 LLM이 생성한 응답을 분류하는 데도 중요한 역할을 하며, 이를 '응답 분류'라고 합니다.
- 프롬프트 및 응답 분류를 위해, 우리는 고품질의 데이터셋을 세심하게 수집했습니다.
- 작은 규모이지만 데이터셋에 지시적으로 튜닝된 'Llama Guard' 모델은 OpenAI Moderation Evaluation 데이터셋과 ToxicChat 같은 기존 벤치마크에서 뛰어난 성능을 보여주며 현재 사용 가능한 콘텐츠 감시 도구들과 맞먹거나 뛰어납니다.
- Llama Guard는 다중 클래스 분류를 수행하고 이진 결정 점수를 생성하는 언어 모델로 기능합니다.
- 또한, Llama Guard의 지시적 미세조정 기능은 태스크 맞춤화 및 출력 포맷 적응을 가능하게 하여 모델 능력을 강화합니다.
- 특별히, 태스크 맞춤화 기능은 특정 사례에 맞게 분류 체계 카테고리를 조절하고, 다양한 분류 체계를 갖는 입력과 함께 제로샷 또는 퓨샷 프롬프팅을 용이하게 합니다.
- 우리는 Llama Guard 모델의 가중치를 공개함으로써 연구자들이 커뮤니티의 AI 안전에 대한 지속적인 필요를 충족시키기 위해 추가적으로 개발하고 적용할 것을 권장합니다.



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
