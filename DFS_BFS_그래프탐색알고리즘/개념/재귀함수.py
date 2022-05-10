#재귀함수
#자기 자신을 호출하는 함수

def fn(v):
    print(v, "번째 출력")
    if v == 10:
        return 
    fn(v+1)
    
fn(1)