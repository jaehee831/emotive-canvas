import streamlit as st 
import cv2
from detect import run, parse_opt
import numpy as np 
import sys 
from pathlib import Path 
import tempfile
import os 
from analyze_house import analyze_house
from analyze_tree import analyze_tree 
from analyze_person import analyze_person

def save_uploaded_file(uploaded_file):
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.jpg') as tmpfile:
            tfile_name = tmpfile.name 
            tmpfile.write(uploaded_file.getvalue())
        return tfile_name 
    except Exception as e:
        return None

def run_detection(htp, image):
    args ={
        'weights': './pretrained-weights/' + htp + '/exp/weights/best.pt',
        'source': image,
        'imgsz': (1280, 1280),
        'project': './output',
        'name': htp,
        'save_txt': True
    }
    results = run(**args)
    save_dir = Path(args['project']) / args['name']
    result_image = list(save_dir.glob('*.jpg'))
    if not result_image:
        return None 
    result_image_path = str(result_image[0])
    return result_image_path

def analysis(htp):
    st.write('{}를 통해 살펴본 당신의 심리 상태는...'.format(htp))

def on_button_click():
    st.session_state.button_clicked = True 

st.markdown('''
    <style>
    .big-font{
            font-size:30px !important;
            font-weight: bold;
            color: #00800;
            text-align: center;
            margin-bottom: 0px;
    }
    .text-style{
            font-size: 15px;
            color: #000000;
            background-color: skyblue;
            padding: 10px;
            border-radius: 3px;
    }
    </style>
            ''', unsafe_allow_html=True)

st.markdown('<p class="big-font">HTP 심리테스트</p>', unsafe_allow_html=True)
select_htp = st.selectbox('어떤 그림을 그려볼까요?', ('집', '나무', '남자사람', '여자사람'))
if select_htp == '집':
    htp = 'House'
    st.markdown('<p class="text-style">HTP 검사 중 집 항목에서는 일반적으로 가족 구성원이나 가족 관계 및 가정 생활에 대한 수검자의 생각, 감정, 소망 및 내적 표상 등이 반영되며, 때로는 가족 관계에서의 자기 지각, 상징적인 의미에서의 자기 표상이나 내적 공상이 투영되기도 합니다.</p>', unsafe_allow_html=True)
elif select_htp == '나무':
    htp = 'Tree'
    st.markdown('<p class="text-style">HTP 검사 중 나무 항목에서는 인생과 성장에 대한 상징이 투사된다고 알려져 있습니다. 여기에는 무의식 수준의 자기 개념과 자기상, 적응 정도, 성취 및 포부 등이 반영됩니다.</p>', unsafe_allow_html=True)
elif select_htp == '남자사람':
    htp = 'PersonM'
    st.markdown('<p class="text-style">HTP 검사 중 사람 항목에서는 무의식적으로 자아가 투영되는 집과 나무와는 달리, 의식적 수준에서의 자아존중감과 대인관계에 대한 개인의 특성을 엿볼 수 있습니다.</p>', unsafe_allow_html=True)
elif select_htp == '여자사람':
    htp = 'PersonF'
    st.markdown('<p class="text-style">HTP 검사 중 사람 항목에서는 무의식적으로 자아가 투영되는 집과 나무와는 달리, 의식적 수준에서의 자아존중감과 대인관계에 대한 개인의 특성을 엿볼 수 있습니다.</p>', unsafe_allow_html=True)
uploaded_file = st.file_uploader('이미지를 업로드하세요.', type=['jpg', 'jpeg', 'png'])

if 'uploaded_image' not in st.session_state:
    st.session_state.uploaded_image = None

if 'button_clicked' not in st.session_state:
    st.session_state.button_clicked = False


if uploaded_file is not None:
    image = save_uploaded_file(uploaded_file)
    if image: 
        st.session_state.uploaded_image = image

if st.session_state.uploaded_image:
    image = st.session_state.uploaded_image
    cols = st.columns(2)
    with cols[0]:
        st.image(image, caption='Uploaded image', use_column_width=True)
    button_detect = st.button('실행')
    if button_detect:
        result_image_path = run_detection(htp, image)
        if result_image_path:
            st.session_state.result_image_path = result_image_path
            result_image = cv2.imread(result_image_path)
            with cols[1]:
                st.image(result_image, caption='Detected Image', use_column_width=True)
            st.write('준비 완료!')
            analysis(htp)
        else:
            st.error('No detected images were found.')
if 'result_image_path' in st.session_state:
    button_analysis = st.button('결과 확인하러 가기')
    if button_analysis:
        result_image_path = st.session_state.result_image_path
        result_image = cv2.imread(result_image_path)
        with cols[1]:
            st.image(result_image, caption='Detected Image', use_column_width=True)
        analysis(htp)
        label_files = list(Path(f'./output/{htp}/labels').glob('*.txt'))
        
        if not label_files:
            st.error('No labels were found')
        else:
            all_data = []
            for file_path in label_files:
                with open(file_path, 'r') as file:
                    data = np.loadtxt(file, dtype=str)
                    all_data.append(data.astype(float))
            all_data = np.concatenate(all_data)
            if htp == 'House':
                score, result = analyze_house(data)
            elif htp == 'Tree':
                score, result = analyze_tree(data)
            else:
                score, result = analyze_person(data)
            # 심리 분석 결과 출력
            st.markdown('<p style="text-align: center; font-weight: bold;">심리 분석 결과</p>', unsafe_allow_html=True)
            if htp == 'House':
                st.markdown('fantasy(공상적), social_withdrawal(대인관계 회피), doubtful(편집증적 경향), dependency(의존성), home_unsatisfaction(가정환경 불만족)')
            if htp == 'PersonF' or htp == 'PersonM':
                st.markdown(
                'aggressive(공격적인, 충동적인, 욕심 많은), depressed(관계 회피적인, 내성적인, 우울한), maladaptive(사회에 적응하지 못한, 열등감, 내적 갈등이 심한), nervous(예민한, 불안한)') 
            st.markdown(f'점수: {score}')
            st.markdown('분석 결과:')
            for line in result:
                st.markdown("<div style='background-color: #add8e6; color:#000000;"
                            "padding: 10px; border-radius: 5px; margin: 5px 0;'>"f"{line}</div>", unsafe_allow_html=True)
