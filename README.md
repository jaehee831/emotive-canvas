# 🎨Emotive Canvas

![logo](/image/logo.png)

Emotive Canvas는 HTP 검사 기반 심리 분석 서비스입니다. 

**HTP test (House-Tree-Person test)**는 인격의 양상을 측정하기 위해 설계된 투영 검사입니다. 이 검사는 뇌손상과 일반적인 정신 기능을 분석하기 위해 사용될 수 있습니다. 검사를 받는 사람은 집, 나무, 사람 그림을 그려보라는 분명하지 않은 짧은 지시를 받으며, 그림을 완성하면 자신이 그린 그림에 대해 설명하라고 요청을 받습니다. 이때 피실험자가 그림을 그릴 때 자신의 내면 세계를 종이 위로 투영하고 있다고 가정합니다. [출처_위키백과](https://ko.wikipedia.org/wiki/%EC%A7%91-%EB%82%98%EB%AC%B4-%EC%82%AC%EB%9E%8C_%EA%B2%80%EC%82%AC)



## 🧑‍🎨Overview

Emotive Canvas는 다음과 같은 방식으로 작동합니다. 

**step 1**. 사용자는 집, 나무, 사람 중 검사를 진행하고자 하는 객체의 그림을 그립니다. 

**step 2**. YOLO v5 기반 object detection model이 사용자의 그림 속 객체를 식별하고, bounding box를 생성합니다. 

**step 3.** 탐지된 객체는 rule-based feature analysis algorithm을 거쳐, 검사 결과가 텍스트로 제공됩니다.   



## 🧑‍🎨Methodology

- 모델 개발에 사용된 dataset은 [AI Hub](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&dataSetSn=71399)에서 제공하는 아동 미술심리 진단을 위한 그림 데이터로, 4개의 class(House, Tree, PersonF, PersonM)로 구성돼 있으며 각각 14,000장씩 총 56,000장의 이미지 데이터셋입니다.

- 각 class(House, Tree, PersonF, PersonM)속 세부 라벨은 아래와 같이 구성되어 있습니다. 

  - House

    | Index | Label  | Index | Label |
    | ----- | ------ | ----- | ----- |
    | 0     | 집전체 | 8     | 길    |
    | 1     | 지붕   | 9     | 연못  |
    | 2     | 집벽   | 10    | 산    |
    | 3     | 문     | 11    | 나무  |
    | 4     | 창문   | 12    | 꽃    |
    | 5     | 굴뚝   | 13    | 잔디  |
    | 6     | 연기   | 14    | 태양  |
    | 7     | 울타리 |       |       |

  

  - Tree

    | Index | Label    | Index | Label  |
    | ----- | -------- | ----- | ------ |
    | 0     | 나무전체 | 7     | 열매   |
    | 1     | 기둥     | 8     | 그네   |
    | 2     | 수관     | 9     | 새     |
    | 3     | 가지     | 10    | 다람쥐 |
    | 4     | 뿌리     | 11    | 구름   |
    | 5     | 나뭇잎   | 12    | 달     |
    | 6     | 꽃       | 13    | 별     |

    

  - PersonF

    | Index | Label    | Index | Label    |
    | ----- | -------- | ----- | -------- |
    | 0     | 사람전체 | 9     | 상체     |
    | 1     | 머리     | 10    | 팔       |
    | 2     | 얼굴     | 11    | 손       |
    | 3     | 눈       | 12    | 다리     |
    | 4     | 코       | 13    | 발       |
    | 5     | 입       | 14    | 단추     |
    | 6     | 귀       | 15    | 주머니   |
    | 7     | 머리카락 | 16    | 운동화   |
    | 8     | 목       | 17    | 여자구두 |

    

  - PersonM

    | Index | Label    | Index | Label    |
    | ----- | -------- | ----- | -------- |
    | 0     | 사람전체 | 9     | 상체     |
    | 1     | 머리     | 10    | 팔       |
    | 2     | 얼굴     | 11    | 손       |
    | 3     | 눈       | 12    | 다리     |
    | 4     | 코       | 13    | 발       |
    | 5     | 입       | 14    | 단추     |
    | 6     | 귀       | 15    | 주머니   |
    | 7     | 머리카락 | 16    | 운동화   |
    | 8     | 목       | 17    | 남자구두 |



- 객체 탐지 모델은 YOLOv5와 Faster-RCNN을 사용했습니다. 이 중 성능이 더 높은 YOLOv5를 적용해 객체 탐지를 진행합니다.

- rule-based feature analysis algorithm은 지배적인 HTP 검사 해석 결과에 따라 구성되었으며, logic은 아래와 같습니다. 

  ![image-20240519005411665](/image/house.PNG)

  ![image-20240519005704078](/image/tree.PNG)

  ![image-20240519002149603](/image/person.png)

  

## 🧑‍🎨Requirement

streamlit 
numpy



## 🧑‍🎨Implement

demo

screenshot

프로젝트에 필요한 username, password



## 🧑‍🎨Hierarchy

```
project-root/
├── folder1/
│   ├── file1.txt
│   └── file2.txt
├── folder2/
│   └── file3.txt
└── README.md
​
```



## 🧑‍🎨Contributors

| name / student id     | role         |
| --------------------- | ------------ |
| Hanna Bae / 20215103  | AI, Frontend |
| Jaehee Lee / 20215160 | AI, Frontend |
| Yunmin Kim / 20225047 | AI, Frontend |
| Yubin Lee  / 20231140 | AI, Frontend |



## 🧑‍🎨References

- 중원대 유경미 교수 강의 자료[ http://contents2.kocw.or.kr/KOCW/document/2019/jungwon/yookyungmi1113/5.pdf](http://contents2.kocw.or.kr/KOCW/document/2019/jungwon/yookyungmi1113/5.pdf),[ http://kocw.xcache.kinxcdn.com/KOCW/document/2019/jungwon/yookyungmi1113/6.pdf](http://kocw.xcache.kinxcdn.com/KOCW/document/2019/jungwon/yookyungmi1113/6.pdf)
- 백원대. "HTP (house-tree-person) 검사 해석체계 구축 및 타당성 제고." 국내박사학위논문 삼육대학교, 2019. 서울.[ https://www.riss.kr/search/detail/DetailView.do?p_mat_type=be54d9b8bc7cdb09&control_no=26719bea71ae11b9ffe0bdc3ef48d419&outLink=K](https://www.riss.kr/search/detail/DetailView.do?p_mat_type=be54d9b8bc7cdb09&control_no=26719bea71ae11b9ffe0bdc3ef48d419&outLink=K)
- 안정애. "어린이의 HTP 검사 반응에 대한 해석과 특징연구." 국내석사학위논문 建國大學校, 2003. 서울.[ https://www.riss.kr/search/detail/DetailView.do?control_no=684f67a4fbce9471&p_mat_type=be54d9b8bc7cdb09&p_submat_type=f1a8c7a1de0e08b8&fulltext_kind=dbbea9ba84e4b1bc&t_gubun=&convertFlag=Y&naverYN=&outLink=&nationalLibraryLocalBibno=&searchGubun=true&colName=bib_t&DDODFlag=&loginFlag=1&url_type=&query=&content_page=&url=&dbName=&dbId=&an=&dbNameDpShort=&pissn=&eissn=](https://www.riss.kr/search/detail/DetailView.do?control_no=684f67a4fbce9471&p_mat_type=be54d9b8bc7cdb09&p_submat_type=f1a8c7a1de0e08b8&fulltext_kind=dbbea9ba84e4b1bc&t_gubun=&convertFlag=Y&naverYN=&outLink=&nationalLibraryLocalBibno=&searchGubun=true&colName=bib_t&DDODFlag=&loginFlag=1&url_type=&query=&content_page=&url=&dbName=&dbId=&an=&dbNameDpShort=&pissn=&eissn=)
