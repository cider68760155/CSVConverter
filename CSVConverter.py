'''
csvファイルを任意の形式のtxtファイルに変換します

Usage: csvConverter.exe [-f FILE] [-o FILE] [INPUT]

Options: 
    -h, --help              ヘルプを表示します
    -f FILE, --format FILE  フォーマットファイルを指定します [default: format.txt]
    -o FILE, --output FILE  出力先ファイルを指定します [default: result.txt]
'''
import csv
import os
import sys
from docopt import docopt


def CheckArgs(args):
    if args['INPUT'] is None:
        print('csvファイルを指定してください')
        sys.exit()
    if not os.path.isfile(args['INPUT']):
        print('csvファイルが見つかりませんでした')
        sys.exit()
    if not os.path.isfile(args['--format']):
        print('フォーマットファイルが見つかりませんでした')
        sys.exit()
    if os.path.isfile(args['--output']):
        print(args['--output'] + 'はすでに存在します')
        print('上書きしますか(y/N)')
        if input() != 'y':
            sys.exit()


def getCsvDictList(fileName):
    try:
        retvals = []
        with open(fileName, encoding="utf_8_sig") as f:
            for row in csv.reader(f):
                retval = {}
                for i, val in enumerate(row):
                    retval[str(i + 1)] = val
                retvals.append(retval)
        return retvals
    except:
        print('csvファイルの読み込みに失敗しました')
        sys.exit()


def main():
    try:
        args = docopt(__doc__)
        CheckArgs(args)
        csvList = getCsvDictList(args['INPUT'])
        with open(args['--format']) as f:
            formatText = f.read()
        outputText = ""
        for row in csvList:
            outputText += formatText % row
        with open(args['--output'], 'w') as f:
            f.write(outputText)
    except Exception as e:
        print('予期せぬエラーが発生しました')
        print(e)


if __name__ == '__main__':
    main()
