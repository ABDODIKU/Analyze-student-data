import json
import random
class Students :
    def __init__(self, filename = "class.json"):
        self.filename = filename
        self.load()
    def load(self) : #تحميل البيانات
        try:
            with open(self.filename,"r") as f:
                self.data = json.load(f)
                self.data.setdefault("students", [])
        except FileNotFoundError:
            self.data = {"students": []}

        self.students = self.data["students"]
    def _save(self): # حفظ البيانات
        with open(self.filename,"w") as f:
            json.dump({"students":self.students},f, indent=4)
    def add_student(self, name, mark):
        new = {"name": name.capitalize(), "marks": mark}  # صححت "marks"
        exists = any(s == new for s in self.students)
        update = any(s["marks"] != new["marks"] and s["name"] == new["name"] for s in self.students)
        if update:
            print("هل تريد تعديل الدرجات")
            choose = int(input("1 - نعم 2- لا"))
            if choose == 1 :
                self.update(new["name"], new["marks"])
        elif not exists:
            self.students.append(new)
            self._save()  # تحفظ البيانات بعد الإضافة
            print(f"{new['name']} تم إضافته بنجاح")
        elif exists :
            print("الطالب موجود بالفعل")

    def update(self, name , new_mark):
        for student in self.students:
            if name.capitalize() == student["name"]:
                student["marks"] = new_mark
                self._save()
    def random_student(self):
        if self.students :    
            random_student = random.choice(self.students)
            print(f'name:{random_student["name"]},marks:{random_student["marks"]}')
        else:
            print("لا يوجد طلاب مسجلون")
    def delete(self, name):
        exist = any(s["name"].capitalize() == name for s in self.students)
        if exist :
            self.students=[s for s in self.students if s["name"]!=name.capitalize()]
            self._save()
        else:
            print("الطالب غير موجود")
    def average(self):
        marks = [m["marks"] for m in self.students]
        if marks :
            average = sum(marks)/len(marks)
            return int(average)
        else:
            print("لا يوجد طلاب مسجلون")
            return 0
    def the_top_mark(self) :
        if not self.students: return []
        marks = [s["marks"] for s in self.students]
        the_top_mark = max(marks)
        the_tops= [s for s in self.students if s["marks"] == the_top_mark]
        return the_tops

