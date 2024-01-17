MessageStorage = [
    {
        "role": "user",
        "content": """
After this, You need to extract keywords for me from this format. I will give input and return output extract keywords for me.

Format 
input : (input)
output : <s>(output)</s>

Example
Me > input : คลีนเซอร์สูตรเนื้อบาล์ม ที่ใช้บนผิวที่แห้ง ก่อนจะเปลี่ยนเป็นออยล์ทำความสะอาดผิวที่เนื้อเนียนละเอียด เมื่อสัมผัสน้ำจะเปลี่ยนเป็นอิมัลชั่นน้ำนมที่ล้างออกได้อย่างง่ายดาย ผิวรู้สึกสมดุลโดยไม่ทิ้งสิ่งตกค้างให้ผิวมันสูตรประสิทธิภาพสูงสามารถทำความสะอาดได้แม้เมคอัพสำหรับผิวรอบดวงตาที่ติดทนนานและสิ่งสกปรกตกค้างรวมถึงมลภาวะในระหว่างวัน ช่วยทำความสะอาดผิวในระดับลึกจึงช่วยให้ผิวโดยรวมแลดูสุขภาพดีขึ้นอย่างเห็นได้ชัด พัฒนาขึ้นเพื่อการทำความสะอาดผิวอย่างหมดจด โดยไม่รบกวนปราการที่ปกป้องผิวตามธรรมชาติ และช่วยทำให้ผิวมีความพร้อมที่จะรับเอาคุณประโยชน์นานาประการจากขั้นตอนดูแลผิวยามค่ำคืนที่จะตามมาสูตรอ่อนโยนต่อผิวจึงช่วยขจัดสิ่งสกปรกและภาระที่ผิวแบกรับไว้ตลอดทั้งวันออกไปอย่างนุ่มนวล ทั้งยังช่วยทำความสะอาดเครื่องสำอางที่ติดทนนาน ฝุ่นควันและมลภาวะอื่นๆ ซึ่งเป็นสาเหตุของผิวที่เสียหายและดูหมอง ทั้งยังช่วยคงสมดุลความชุ่มชื้นตามธรรมชาติและไม่ทำให้ผิวแห้งตึงอีกด้วย
Your > output : <s>คลีนเซอร์,เนื้อบาล์ม,ทำความสะอาดผิว,น้ำนม,สิ่งสกปรก,มลภาวะ,สูตรอ่อนโยน,หมดจด</s>


Me > input : เจลครีมทาหน้าสำหรับกลางวันที่เติมความชุ่มชื้น อุดมไปด้วยกรดไฮยาลูโรนิก ให้ความชุ่มชื้นอย่างเข้มข้นและทำให้ผิวอิ่มเอิบ ในขณะเดียวกันก็ทำให้ผิวของคุณดูแมตต์ หัวใจสำคัญของสูตรนี้ ที่พัฒนาโดย ช่วยเพิ่มกลไกการให้ความชุ่มชื้นตามธรรมชาติของผิวและรักษาความชุ่มชื้นของผิว เนื้อแมตต์ที่สดชื่นจะละลายเข้าสู่ผิวทันที ทิ้งความอวบอิ่ม เปล่งปลั่ง และเบาสบาย ผิวชุ่มชื้นอิ่มน้ำ
Your > output : <s>ความชุ่มชื้น,เนื้อแมตต์,สดชื่น,เบาสบาย,เจลครีมทาหน้า,ไฮยาลูโรนิก</s>

Your Answer with output : <s>(output)</s>
""",
    },
    {"role": "assistant", "content": "Ok I will answer with output : <s>(output)</s>"},
    {
        "role": "user",
        "content": "input : แปรงแต่งหน้าสำหรับปัดแก้มขนแปรงมีลักษณะกลมมนขนาดพอเหมาะกับรูปแก้มใช้เกลี่ยสีบลัชออนให้กระจายบริเวณแก้มหรือโหนกแก้มได้ตามต้องการด้ามแปรงสีมิ้นท์น้ำหนักเบาแข็งแรงจับได้ถนัดมือ",
    },
    {
        "role": "assistant",
        "content": "output : <s>แปรงแต่งหน้า,ปัดแก้ม,กลมมน,สีมิ้นท์,น้ำหนักเบา</s>",
    },
    {
        "role": "user",
        "content": "input : ซิก้า สลีปปิ้งมาสก์ชนิดแรกของโลกที่ใช้ส่วนผสมของยีสต์ป่า ส่วนผสมที่คัดมาแล้วว่า ฟื้นบำรุงผิวอัตโนมัติ เสริมปราการปกป้องผิว ลดการระคายเคืองจากปัจจัยภายนอก",
    },
    {
        "role": "assistant",
        "content": "output : <s>ซิก้า,สลีปปิ้งมาสก์,ยีสต์ป่า,ปราการ,ปัจจัยภายนอก</s>",
    },
]