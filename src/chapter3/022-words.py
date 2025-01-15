week = input("请输入中文：")
data = {
    "星期一": "Monday，读音 ['mʌndi, 'mʌndei]，英文缩写 Mon.",
    "星期二": "Tuesday，读音 ['tju:zdi]，英文缩写 Tue。",
    "星期三": "Wednesday，读音 ['wenzdei, 'wenzdi]，英文缩写 Wed。",
    "星期四": "Thursday，读音 ['θə:zdi]，英文缩写 Thur。",
    "星期五": "Friday，读音 ['fraidi]，英文缩写 Fri。",
    "星期六": "Saturday，读音 ['sætədi]，英文缩写 Sat。",
    "星期日": "Sunday，读音 ['sʌndi]，英文缩写 Sun。"
}
print(data.get(week, "词典中未收录该词"))
