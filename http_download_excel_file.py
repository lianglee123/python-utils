# -*- coding:utf8 -*-
import io
import urllib

import xlwt
from flask import Flask, Response

app = Flask(__name__)


def create_template():
    headers = [
        u"第一列",
        u"第二列",
        u"第三列",
    ]
    memory_file = io.BytesIO()

    workbook = xlwt.Workbook(encoding="utf8")
    sheet = workbook.add_sheet("Sheet1")

    style = xlwt.XFStyle()
    font = xlwt.Font()
    font.height = 300
    style.font = font

    for i, header in enumerate(headers):
        sheet.write(r=0, c=i, label=header, style=style)
        sheet.col(i).width = 9000
    workbook.save(memory_file)

    memory_file.seek(0)
    return memory_file


@app.route("/download")
def hello():
    template_file = create_template()
    data = template_file.read()
    template_file.close()
    file_name = urllib.quote_plus(u"模板文件.xls".encode("utf8"))
    resp = Response(data,
                    headers={
                        "Content-Disposition": "attachment; filename=%s;filename*=utf-8''%s"
                                               % (file_name, file_name),
                        "Content-Type": "application/vnd.ms-excel"
                    })
    return resp


if __name__ == "__main__":
    app.run("127.0.0.1", port=8080, debug=True)
