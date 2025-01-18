# KUR-dev-machine
# map <F8> :wa<CR>:lcd /home/kur/dev/SickZil-Machine/src<CR>:!python main.py<CR>
# map <F5> :wa<CR>:lcd /home/kur/dev/SickZil-Machine/test<CR>:!pytest -vv<CR>
# KUR-LAB-MACHINE
# map <F8> :wa<CR>:lcd /home/kur/dev/szmc/SickZil-Machine/src<CR>:!python main.py<CR>
# map <F5> :wa<CR>:lcd /home/kur/dev/szmc/SickZil-Machine/test<CR>:!pytest -vv<CR>

import locale
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine
import gui
import consts
import core


def load_based_on_locale():
    # 현재 시스템의 기본 언어와 인코딩을 가져옵니다.
    language, encoding = locale.getdefaultlocale()

    # 언어 코드를 단축하고 인코딩이 None인 경우 기본값 설정
    lang_code = language[:2].lower() if language else 'en'  # 언어가 없는 경우 영어를 기본값으로

    # config 파일 이름을 생성하여 로드
    config_file = f'../resource/config-{lang_code}.json'.replace('-en.', '.')
    print(f"load (config_file)")

    try:
        consts.load_config(config_file)
        print(f"Config loaded: {config_file}")
    except FileNotFoundError:
        print(f"Config file not found: {config_file}\nload default...")
        consts.load_config("../resource/config.json")


if __name__ == '__main__':
    load_based_on_locale()
    core.set_limits(
        consts.config['seg_limit'],
        consts.config['compl_limit']
    )

    app = QApplication(sys.argv)

    engine = QQmlApplicationEngine()
    main_window = gui.MainWindow(engine)

    sys.exit(app.exec_())
