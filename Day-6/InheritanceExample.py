class Algebra:
    def add(a,b):
        return a+b
class TotalMaths(Algebra):
    def mul(a,b):
        return a*b    
class AllSubjects(TotalMaths):
    def div(a,b):
        return a/b
        
print(AllSubjects.add(5,6))
print(AllSubjects.mul(5,6))
print(AllSubjects.div(4,2))
