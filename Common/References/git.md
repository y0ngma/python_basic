# git 형상관리 절차
1. fork
1. git clone fork된것
1. master에서 수정
1. branch에서 작업시 merge해줘야함
1. fork-master으로 push 
1. 각 개발자는 쓰기권한이 없으므로 PR발행 (Pull request)
1. 쓰기 권한을 가진 관리자가 각 개발자의 Origin Remote Repository에 모아진 commit/push을 검토
1. Upstream에 merge 실행
1. 충돌 없이 하나의 원본에 가장 효율적인 코드가 추가됨

# 저장소 종류 개요
- Upstream (Remote) Repository
    - 형상 마스터가 원본소스 관리
    - 각 개인이 직접 원본 수정 불가
    - PR발행을 통해 원본에 contribute(원본수정)
    - fork를 통해 원본을 Origin으로 가져올수있음

- Origin (Remote) Repository
    - 개인이 commit / push 하면 올라가게되는곳
    - 직접 원본 수정가능한곳
    - Fork 해 오면 이쪽으로 오게됨
    
- Local Repository
    - git clone 해오는곳
    - (fork 된) 개인 코드 수정 가능
    - 개인의 Origin Repository에 push가능 후 다시 회사의 Upstream에 Pull Request발행하여 원본소스에 merge한다(contribute).



# Upstream Remote Repository
1. 원하는 github에 가서 fork 해오기

1. 자신의 

```bash
# git clone 원본
git clone https://github.com/baniota/git-upstream.git

# git remote add 원하는이름 깃주소 
git remote add fork-master https://github.com/y0ngma/git-upstream.git


admin@DESKTOP-3VULP62 MINGW64 /c/Repository/git-upstream (master)
git remote -v
git remote rename origin fork-master
# git remote rename 바꿀이름 새이름
# 확인


git pull from upstream # 최종버전 받기

```
1. 원격저장소 추가하기
```bash
git
```


# Local Repository
## 0. 경로만들기
- 원하는 경로의 폴더에서 우클릭으로 git bash를 실행한다
    ```bash
    # 현재 작업경로확인
    pwd
    
    # 디렉토리 만들기
    mkdir manual
    
    # 추가된 내용 확인
    ls
    
    # 추가된 폴더로 접근
    cd manual
    
    # 깃설정
    git init
    
    # 숨긴파일까지 확인가능
    ls -al
    
    # (optional) Virtual Studio Code 실행
    code .
    ```
- vim을 이용한 파일 수정
    ```bash
    # vim에 조회모드로 기본접속
    vi work.txt
    # 수정내용 확인하기
    cat work.txt
    ``` 
    - 조회 모드
        - search, replace, save, exit
            - :q! 하면 저장 안하고 빠져나올 수 있음 
            - :wq! 하면 저장하고 빠져 나옴 

    - 편집 모드
        - 파일내용 수정
        - 조회모드에서 i 또는 a로 접속
            - dd : 한줄씩 지워짐 
            - de : 두줄씩 지워짐
            - esc키 눌러서 조회모드로 빠져나올 수 있음 

## 1. 브런치를 만들고자 하는 시점으로 checkout 한다
- `git branch` 하면 현재 브런치 목록이 나온다
    ```bash
    git branch
    git checkout master
    ```
## 2. 브런치를 만들고 내용을 확인해본다
- ls 하면 master와 같은 내용이 있음을 확인가능
    ```bash
    git branch home
    git branch
    ls
    ```
## 3. 브런치로 checkout해서 작업한다
- `git branch` 하면 생성된 브런치 확인가능
    ```bash
    git checkout home
    vi test_home.txt
    ```
## 4. 작업내용을 stage 한다.
- `add .`은 해당작업경로의 모든 변동사항을 stage하는듯 하다
- 방금 작업한 파일명을 적으면 그것만 stage된다.
    ```bash
    git add .
    git add test_home.txt
    ```
## 5. 작업내용을 commit 한다.
- `-am`으로 하면 add도 동시에 하는것이다
    - 다만, 최초실행시에는 작동하지 않는다
    ```bash
    git commit -m 'I made home branch!'
    git commit -am 'I made home branch!'
    ```
- 특정 시점으로 돌아가는 방법
    ```bash
    # admin@DESKTOP-3VULP62 MINGW64 ~/pictures/manual-merge (master)
    git log --all --graph --oneline
    * 745db65 (HEAD -> master, o2) o2 work 2
    * d78557f work 1

    # 위 log에서 확인한 복원지점 번호를 기입한다
    git reset --hard 745db65
    ```
## 6. 원격저장소에 push 한다
- 원격저장소 목록을 확인후
- `git push 목적저장소 브런치명` 과 같이 적는다
    ```bash
    git remote -v
    git push fork-master home
    ```
## 7. merge
- `git branch`로 현재 checkout된것을 확인한다
- 원하는 브런치로 checkout한 후 
- `git merge 목표브런치`를 기입한다
    ```bash
    git checkout master
    git merge home
    ```
## 8. push
- 혹시 로컬과 원격의 내용이 다르다면 pull먼저 해준 후 push해주면 오류가 없어진다.
- github등에서 merge된것을 확인 가능 하다.
    ```bash
    git pull fork-master master
    git push fork-master master
    ```
# Original Remote Repository