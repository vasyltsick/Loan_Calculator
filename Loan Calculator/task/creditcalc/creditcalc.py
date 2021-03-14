import math
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", choices=['annuity', "diff"])
    parser.add_argument("--payment", type=float)
    parser.add_argument("--principal", type=float)
    parser.add_argument("--periods", type=int)
    parser.add_argument("--interest", type=float)
    args = parser.parse_args()

    if not check_parameters(args):
        return

    args.interest = args.interest / (100 * 12)
    overpayment = 0
    if args.type == "annuity":
        if args.periods is None:
            result = calc_number_monthly_payments(p=args.principal, m=args.payment, i=args.interest)
            print(f"It will take {convert_months(result)} to repay this loan!")
            overpayment = round(args.payment * result - args.principal)
        elif args.payment is None:
            result = calc_annuity_monthly_payment_amount(p=args.principal, n=args.periods, i=args.interest)
            print(f"Your annuity payment = {result}!")
            overpayment = round(result * args.periods - args.principal)
        elif args.principal is None:
            result = calc_loan_principal(a=args.payment, n=args.periods, i=args.interest)
            print(f"Your loan principal = {result}!")
            overpayment = round(args.payment * args.periods - result)
    elif args.type == "diff":
        overpayment = calc_differentiated_payment(p=args.principal, n=args.periods, i=args.interest)
    print(f"Overpayment = {overpayment}")


def check_parameters(args):
    if args.type is None or \
            args.interest is None or \
            len(vars(args)) < 4 or \
            args.type == "diff" and args.payment is not None:
        print("Incorrect parameters")
        return False
    for arg in vars(args).values():
        try:
            if int(arg) < 0:
                print("Incorrect parameters")
                return False
        except ValueError:
            continue
        except TypeError:
            continue
    return True


def calc_number_monthly_payments(p, i, m):
    n = math.ceil(math.log((m / (m - i * p)), 1 + i))
    return n


def calc_annuity_monthly_payment_amount(p, n, i):
    a = math.ceil(p * i * (1 + i) ** n / ((1 + i) ** n - 1))
    return a


def calc_loan_principal(a, n, i):
    p = math.ceil(a / ((i * (1 + i) ** n) / ((1 + i) ** n - 1)))
    return p


def calc_differentiated_payment(p, n, i, overpayment=0):
    for m in range(1, n + 1):
        d = math.ceil(p / n + i * (p - (p * (m - 1)) / n))
        print(f"Month {m}: payment is {d}")
        overpayment += d
    return round(overpayment - p)


def correct_plural_form(number: int, noun: str):
    if noun == "month":
        return noun if number % 12 == 1 else noun + "s"
    elif noun == "year":
        return noun if number // 12 == 1 else noun + "s"


def convert_months(number):
    month = correct_plural_form(number, "month")
    year = correct_plural_form(number, "year")
    if number < 12:
        output = f"{number} {month}"
    elif number % 12 == 0:
        output = f"{number // 12} {year}"
    else:
        output = f"{number // 12} {year} and {number % 12} {month}"
    return output


if __name__ == '__main__':
    main()
