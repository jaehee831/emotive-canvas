import numpy as np 

def analyze_house(data):
    sorted_idx = np.argsort(data[:, 0])
    sorted_data = data[sorted_idx]

    label = sorted_data[:, 0]
    X = np.array(sorted_data[:, 1], dtype=np.float64)
    Y = np.array(sorted_data[:, 2], dtype=np.float64)
    W = np.array(sorted_data[:, 3], dtype=np.float64)
    H = np.array(sorted_data[:, 4], dtype=np.float64)
    print(X, Y, W, H )
    n_data = len(label)

    # fantasy(공상적), social_withdrawal(대인과계 회피), doubtful(편집증적 경향), dependency(의존성), home_unsatisfaction(가정환경 불만족)
    score = np.zeros((5))
    result = ['HTP 검사 중 집 항목에서는 일반적으로 가족 구성원이나 가족 관계 및 가정 생활에 대한 수검자의 생각, 감정, 소망 및 내적 표상 등이 반영되며,\n때로는 가족 관계에서의 자기 지각, 상징적인 의미에서의 자기 표상이나 내적 공상이 투영되기도 합니다.\n']

    # 0:집전체, 1:지붕, 2:집벽, 3:문, 4:창문, 5:굴뚝, 6:연기, 7:울타리
    # 8:길, 9:연못, 10:산, 11:나무, 12:꽃, 13: 잔디, 14:태양

    house_size = W[0] * H[0]
    roof_size = W[1] * H[1]
    wall_size = W[2] * H[2]
    door_size = W[3] * H[3]
    window_size = W[4] * H[4]
    chimney_size = W[5] * H[5]
    smoke_size = W[6] * H[6]
    fence_size = W[7] * H[7]
    road_size = W[8] * H[8]
    pond_size = W[9] * H[9]
    mountain_size = W[1] * H[10]
    tree_size = W[11] * H[11]
    flower_size = W[12] * H[12]
    grass_size = W[13] * H[13]
    sun_size = W[14] * H[14]

    roof_coords = (X[1], Y[1], W[1], H[1])
    door_coords = [(X[3], Y[3], W[3], H[3])]
    window_coords = [(X[4], Y[4], W[4], H[4])]
    print('label 4의 점수')
    print(sum(label == 4))

    """ a 내부에 b의 중심이 있는지 확인 """
    def coord(a, b):
        ax, ay, aw, ah = a
        bx, by, _, _ = b
        return (ax - aw / 2 <= bx <= ax + aw / 2) and \
              (ay - ah / 2 <= by <= ay + ah / 2)


    # 집 전체
    if house_size < 0.2:           # 집이 멀리 보이는 시야
        score[1] += 2          # 대인관계 위축
        score[4] += 2        # 가정생활 불만족
        print("집을 너무 작게 그린 경우, 대인관계에 위축되어 있고, 가정생활에 만족하지 못하고 있다고 해석됩니다.")
        result.append("집을 너무 작게 그린 경우, 대인관계에 위축되어 있고, 가정생활에 만족하지 못하고 있다고 해석됩니다.")


    # 지붕 (정신생활, 공상적인 영역의 상징.)
    if roof_size > house_size * 0.8:    # 지붕이 집에 비해 크면
        score[0] += 1               # 공상의 정도가 크고,
        score[1] += 1     # 대인관계에 회피적이다
        print("지붕의 크기는 공상을 통해 자기만족을 찾으려는 정도를 나타내며, 지붕이 집보다 큰 경우 외면적인 대인관계로부터 회피적일 수 있습니다.")
        result.append("지붕의 크기는 공상을 통해 자기만족을 찾으려는 정도를 나타내며, 지붕이 집보다 큰 경우 외면적인 대인관계로부터 회피적일 수 있습니다.")

    for coords in door_coords + window_coords:
        if coord(roof_coords, coords):  # 지붕에 문이나 창문이 있으면
            score[0] += 2             # 공상의 정도가 크다
            print("지붕 위에 문이나 창문이 있으면, 자신만의 공상세계에 빠져있을 확률이 높다고 해석됩니다.")
            result.append("지붕 위에 문이나 창문이 있으면, 자신만의 공상세계에 빠져있을 확률이 높다고 해석됩니다.")
            break                      # 반복 중단

    # 문 (수검자의 환경과의 접촉, 대인관계에 대한 태도와 관련)
    if door_size > 0.1:          # 문 크기가 지나치게 크면
        score[3] += 2               # 타인에게 의존적
        print("문이 지나치게 클 경우, 타인에게 과도하게 의존적임을 의심해 볼 수 있습니다.")
        result.append("문이 지나치게 클 경우, 타인에게 과도하게 의존적임을 의심해 볼 수 있습니다.")

    if door_size < house_size * 0.1:  # 문이 집에 비해 너무 작을때
        score[1] += 1        # 대인관계에 위축되어 있다.
        print("집과 창문에 비해 문이 지나치게 작을 경우, 대인관계에서 위축되었음을 의심해볼 수 있습니다.")
        result.append("집과 창문에 비해 문이 지나치게 작을 경우, 대인관계에서 위축되었음을 의심해볼 수 있습니다.")


    # 창문 (외부환경과 접촉할 수 있는 제2의 통로)
    if sorted_data[label == 4] is None:   # 창문이 없으면
        score[2] += 2      # 편집증적 경향이 있다.
        score[1] += 2      # 대인관계에 위축되어 있다.
        print("창문이 없는 경우, 대인관계에 위축되어있으며 편집증적 경향을 의심해 볼 수 있습니다.")
        result.append("창문이 없는 경우, 대인관계에 위축되어있으며 편집증적 경향을 의심해 볼 수 있습니다.")

    if sum(label == 4) > 2:       # 창문이 많으면
        score[3] += 1             # 의존적인 경향
        print("창문이 많을 경우, 의존적인 경향이 있다고 해석됩니다.")
        result.append("창문이 많을 경우, 의존적인 경향이 있다고 해석됩니다.")

        # 굴뚝
    if chimney_size < house_size * 0.01:    # 집에 비해 너무 작은 굴뚝
        score[4] += 1                                # 가정생활 불만족
        print("굴뚝이 너무 작을 경우, 가정환경에서 따뜻함을 충분히 느끼지 못하고 있는 상태로 해석됩니다.")
        result.append("굴뚝이 너무 작을 경우, 가정환경에서 따뜻함을 충분히 느끼지 못하고 있는 상태로 해석됩니다.")

    # 연기
    if smoke_size > chimney_size * 0.8:     # 연기가 많이 나올 때
        score[2] += 2                                  # 편집증적 경향
        score[4] += 1                                # 가정생활 불만족
        print("굴뚝에서 연기가 많이 나올 경우, 마음속에 긴장이 존재하고, 가정환경 내에서 갈등이 있다고 해석됩니다.")
        result.append("굴뚝에서 연기가 많이 나올 경우, 마음속에 긴장이 존재하고, 가정환경 내에서 갈등이 있다고 해석됩니다.")

        # 그 외
    if sum(label == 7) > 0:      # 울타리가 있으면
        score[2] += 1      # 대인관계 위축
        print("울타리를 그린 경우, 대인관계에 위축되어 있고, 안전을 방해받고 싶지 않은 생각이 욕구가 강하다고 해석됩니다.")
        result.append("울타리를 그린 경우, 대인관계에 위축되어 있고, 안전을 방해받고 싶지 않은 생각이 욕구가 강하다고 해석됩니다.")

    if sum(label == 8) + sum(label == 12) > 0:      # 집 주위에 길이 있거나 꽃이 있으면
        score[1] += 1                              # 사회적 회피 극복
        print("길이나 꽃을 함께 그린 경우, 타인과 상호작용에 시간이 걸리지만, 나중에는 상호 신뢰감을 형성하게 된다고 해석됩니다.")
        result.append("길이나 꽃을 함께 그린 경우, 타인과 상호작용에 시간이 걸리지만, 나중에는 상호 신뢰감을 형성하게 된다고 해석됩니다.")

        # fantasy(공상적), social_withdrawal(대인과계 회피), doubtful(편집증적 경향), dependency(의존성), home_unsatisfaction(가정환경 불만족)

    if score[0] == 0:
      result.append('공상적이지 않고 현실적이며 자기 만족을 잘 찾는 사람으로 보입니다. ')
    if score[1] == 0:
      result.append('대인관계에서 회피적이지 않고 적극적이며 사교적인 사람으로 보입니다. ')
    if score[2] == 0:
      result.append('편집증적 경향이 없으며 신뢰감을 가지고 있는 사람으로 보입니다. ')
    if score[3] == 0:
      result.append('의존적이지 않고 독립적이며 자기 주도적인 사람으로 보입니다. ')
    if score[4] == 0:
      result.append('가정환경에 대해 만족하며 안정감을 느끼는 사람으로 보입니다. ')

    return score, result