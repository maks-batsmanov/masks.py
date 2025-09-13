import masks

def mask_account_card(card_or_account: str) -> str:
    '''Функция обрабатывает информацию о картах и счетах'''
    if 'счет' in card_or_account.lower():
        parts = card_or_account.split()
        return f'{parts[0]} {masks.get_mask_account(parts[1])}'
    else:
        parts = card_or_account.split()
        if len(parts) == 2:
            return f'{parts[0]} {masks.get_mask_card_number(parts[1])}'
        else:
            return f'{parts[0]} {parts[1]} {masks.get_mask_card_number(parts[2])}'
