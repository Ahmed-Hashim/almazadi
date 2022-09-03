
cati=['Car','House','Job','Food','Phone','School','Computer','Garden']
cat=['car','house','job','food','phone','school','computer','garden']
for z in cat:
    file= open(f'./Frontend/links/link{z}.txt','r')
    for i in file:
        message="إذا كنت تحتاج إلى عدد أكبر من الفقرات يتيح لك مولد النص العربى زيادة عدد الفقرات كما تريد، النص لن يبدو مقسما ولا يحوي أخطاء لغوية، مولد النص العربى مفيد لمصممي المواقع على وجه الخصوص، حيث يحتاج العميل فى كثير من الأحيان أن يطلع على صورة حقيقية لتصميم الموقع."
        link=i.rstrip()
        cati=z.capitalize()
        print(cati)

