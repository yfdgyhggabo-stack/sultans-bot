import random
import time

def generate_luhn_card(prefix, length=16):
    card = [int(digit) for digit in prefix]
    while len(card) < length - 1:
        card.append(random.randint(0, 9))
    
    def luhn_checksum(card_digits):
        sum_val = 0
        is_even = True
        for digit in reversed(card_digits):
            if is_even:
                digit *= 2
                if digit > 9:
                    digit -= 9
            sum_val += digit
            is_even = not is_even
        return (sum_val * 9) % 10

    card.append(luhn_checksum(card))
    return "".join(map(str, card))

def generate_test_card(card_type="visa"):
    if card_type.lower() == "visa":
        prefix = "4"; length = 16
    elif card_type.lower() == "mastercard":
        prefix = str(random.choice(range(51, 56))); length = 16
    else:
        prefix = "4"; length = 16

    card_number = generate_luhn_card(str(prefix), length)
    formatted_card = " ".join([card_number[i:i+4] for i in range(0, len(card_number), 4)])
    month = f"{random.randint(1, 12):02d}"
    year = f"{random.randint(27, 32)}"
    cvv = f"{random.randint(100, 999)}"
    
    return {
        "Card Number": formatted_card,
        "Expires": f"{month}/{year}",
        "CVV": cvv
    }

# حلقة تكرارية لا نهائية لتوليد البطاقات باستمرار
print("--- بدء عملية التوليد المستمر (إلى ما لا نهاية) ---")
counter = 1

while True:
    card_info = generate_test_card("visa")
    print(f"\n[محاولة رقم {counter}]")
    for key, value in card_info.items():
        print(f"{key}: {value}")
    
    counter += 1
    # الانتظار لمدة ثانية واحدة بين كل محاولة وأخرى (يمكنك تعديل الرقم حسب رغبتك)
    time.sleep(1)
