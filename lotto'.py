import random

PRINTER_LOTTO_PRICE = "로또의 가격은 개당 1000원입니다"
PRINTER_INPUT_LOTTO_TOTAL_PRICE = "얼마의 로또를 구매하시겠습니까? 구입금액을 입력해 주세요: "
PRINTER_AMOUNT_LOTTO_BOUGHT = "장의 로또를 구입하셨습니다."
PRINTER_INPUT_WINNING_NUMBER = "지난 주 당첨 번호를 공백으로 구분하여 입력해주세요: "
LOTTO_PRICE = 1000
LOTTO_NUMBER_COUNT = 6

ERROR_LEAST_PRICE = "로또의 최소 가격은 1000원입니다."

def print_lotto_price():
    print(PRINTER_LOTTO_PRICE)


def input_price_bought():
    total_price_bought = int(input(PRINTER_INPUT_LOTTO_TOTAL_PRICE))
    if total_price_bought == 0:
        print(ERROR_LEAST_PRICE)
        exit(1)
    return total_price_bought


def get_amount_lotto_bought(price_bougth):
    amount = int(price_bougth / LOTTO_PRICE)
    print(amount, PRINTER_AMOUNT_LOTTO_BOUGHT)
    return amount


def get_random_lotto_num(amount_lotto, lotto_num_set):
    for i in range(amount_lotto):
        for j in range(LOTTO_NUMBER_COUNT):
            lotto_num_set[i][j] = random.randint(1, 46)


def print_lotto_num_set(amount_lotto, lotto_num_set):
    for k in range(amount_lotto):
        print(lotto_num_set[k])


def input_winning_lotto():
    winning_num = list(map(int, input(PRINTER_INPUT_WINNING_NUMBER).strip().split()))[:LOTTO_NUMBER_COUNT]
    return winning_num


def count_lotto_winning_num(winning_lotto, lotto_num_set, amount_lotto):
    count = [0 for idx in range(amount_lotto)]
    for num_set in range(amount_lotto):
        for num in range(LOTTO_NUMBER_COUNT):
            if winning_lotto[num] == lotto_num_set[num_set][num]:
                count[num_set] += 1
    return count


def print_lotto_result(score):
    result = lotto_result(score)
    print(4,'등(',3,'개가 맞을 때) - 5000원 - ',result[3])
    print(3,'등(',4,'개가 맞을 때) - 20000원 - ',result[2])
    print(2,'등(',5,'개가 맞을 때) - 100000원 - ',result[1])
    print(1,'등(',6,'개가 맞을 때) - 5000000원 - ',result[0])
    return result
    

def lotto_result(score):
    place = [0 for idx in range(4)]
    for idx in range(len(score)):
        if score[idx] == 6:
            place[0] += 1
        elif score[idx] == 5:
            place[1] += 1
        elif score[idx] == 4:
            place[2] += 1
        elif score[idx] == 3:
            place[3] += 1
    return place


def get_earning_rate(result, amount_lotto):
    sum = 5000*result[3] + 20000*result[2] + 100000*result[1] + 5000000*result[0]
    return sum/(amount_lotto*LOTTO_PRICE)
    

def print_earning_rate(earning_rate):
    print('수익률 : ',earning_rate)


def main():
    # 로또 개당 가격 출력
    print_lotto_price()

    # 구입금액 입력받기
    price_bougth = input_price_bought()

    # 구입한 로또 개수 출력 & 저장
    amount_lotto = get_amount_lotto_bought(price_bougth)

    # 로또 초기화
    lotto_num_set = [[0 for x in range(LOTTO_NUMBER_COUNT)]for y in range(amount_lotto)]

    # 로또 랜덤 생성
    get_random_lotto_num(amount_lotto, lotto_num_set)
    print_lotto_num_set(amount_lotto,lotto_num_set)

    # 지난 주 당첨 결과 출력
    winning_lotto = input_winning_lotto()
    
    # 로또 당첨 결과를 출력하기
    score = count_lotto_winning_num(winning_lotto, lotto_num_set, amount_lotto)
    result = print_lotto_result(score)

    # 수익률 계산
    earning_rate = get_earning_rate(result, amount_lotto)
    print_earning_rate(earning_rate)
    


if __name__ == "__main__":
    main()