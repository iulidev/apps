from enum import Enum

CodesToCheck2 = Enum(
    value='Validation Code',
    names=('INRANGE, TOOSMALL, TOOBIG'),
)


class CodesToCheck(Enum):
    INRANGE = 1
    TOOSMALL = 2
    TOOBIG = 3


def main():
    y = 3
    # Print single member
    print('Member: ', CodesToCheck.INRANGE)

    # Iterate over all the members
    print(f'\nAll members: {CodesToCheck.__class__.__name__}')
    for member in CodesToCheck:
        print(member.name, '=', member.value)
    day = int(input('Enter day:'))
    if day in range(1, 32):
        check = CodesToCheck.INRANGE
    elif day < 1:
        check = CodesToCheck.TOOSMALL
    else:
        check = CodesToCheck.TOOBIG
    print()
    print(check, ' and the name is ', check.name)


if __name__ == '__main__':
    main()
