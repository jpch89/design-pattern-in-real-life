class Page:
    '电子书一页的内容'

    def __init__(self, page_num):
        self.__page_num = page_num

    def get_content(self):
        return '第 ' + str(self.__page_num) + ' 页的内容...'


class Catalog:
    '目录结构'

    def __init__(self, title):
        self.__title = title
        self.__chapters = []
        self.set_chapter('第一章')
        self.set_chapter('第二章')

    def set_chapter(self, title):
        self.__chapters.append(title)

    def show_info(self):
        print('标题：' + self.__title)
        for chapter in self.__chapters:
            print(chapter)


class IBook:
    '电子书文档类的接口'

    def parse_file(self, file_path):
        pass

    def get_catalog(self):
        pass

    def get_page_count(self):
        pass

    def get_page(self):
        pass


class TxtBook(IBook):
    'txt解析类'

    def parse_file(self, file_path):
        # 模拟文档的解析
        print(file_path + ' 文件解析成功')
        self.__page_count = 500
        return True

    def get_catalog(self):
        return Catalog('txt电子书')

    def get_page_count(self):
        return self.__page_count

    def get_page(self, page_num):
        return Page(page_num)


class EpubBook(IBook):
    'epub解析类'

    def parse_file(self, file_path):
        # 模拟文档的解析
        print(file_path + ' 文件解析成功')
        self.__page_count = 800
        return True

    def get_catalog(self):
        return Catalog('Epub电子书')

    def get_page_count(self):
        return self.__page_count

    def get_page(self, page_num):
        return Page(page_num)


class Outline:
    '第三方pdf解析库的目录类'

    pass


class PdfPage:
    'pdf页'

    def __init__(self, page_num):
        self.__page_num = page_num

    def get_page_num(self):
        return self.__page_num


class ThirdPdf:
    '第三方pdf解析库'

    def __init__(self):
        self.__page_size = 0

    def open(self, file_path):
        print('第三方解析pdf文件：' + file_path)
        self.__page_size = 1000
        return True

    def get_outline(self):
        return Outline()

    def page_size(self):
        return self.__page_size

    def page(self, index):
        return PdfPage(index)


class PdfAdapterBook(ThirdPdf, IBook):
    'Pdf解析类'

    def parse_file(self, file_path):
        # 模拟文档的解析
        rtn = super().open(file_path)
        if rtn:
            print(file_path + ' 文件解析成功')
        return rtn

    def get_catalog(self):
        outline = super().get_outline()
        print('将Outline结构的目录转换成Catolog结构的目录')
        return Catalog('pdf电子书')

    def get_page_count(self):
        return super().page_size()

    def get_page(self, page_num):
        page = self.page(page_num)
        print('将PdfPage的面对象转换成Page的对象')
        return Page(page.get_page_num())


# 导入 os 库
import os

class Reader:
    '阅读器'

    def __init__(self, name):
        self.__name = name
        self.__file_path = ''
        self.__cur_book = None
        self.__cur_page_num = -1

    def __init_book(self, file_path):
        self.__file_path = file_path
        # 返回元组 (root, ext)
        ext_name = os.path.splitext(file_path)[1].lower()
        if ext_name == '.epub':
            self.__cur_book = EpubBook()
        elif ext_name == '.txt':
            self.__cur_book = TxtBook()
        elif ext_name == '.pdf':
            self.__cur_book = PdfAdapterBook()
        else:
            self.__cur_book = None

    def open_file(self, file_path):
        self.__init_book(file_path)
        if not self.__cur_book:
            rtn = self.__cur_book.parse_file(file_path)
            if rtn:
                self.__cur_page_num = 1
            return rtn
        return False

    