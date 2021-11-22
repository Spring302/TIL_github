# hello git

## git 명령어 요약

- clone: 원격 저장소 복사
- add: 스테이지 영역에 작업 파일 추가
- commit: 세이브, 스테이지 영역의 파일들을 가지고 커밋(=세이브)를 만들 수 있다.
- push: 원격 저장소에 커밋을 업로드한다.

## 브랜치 변경하기

- 브랜치 : 기존 내용을 유지한채 새로운 내용을 추가하고 싶을 때 사용
- 체크아웃 : 특정 브랜치(혹은 커밋) 으로 돌아가고 싶을 때 사용
- 소스트리의 체크아웃: 브랜치 이름을 더블 클릭하는 것만으로 체크아웃 가능

## 새로운 브랜치 만들기 

- 원하는 커밋을 만들고 우클릭, 새 브랜치 이름 입력하면 커밋으로부터 브랜치가 생긴다.

## 원하는 브랜치로 돌아가기

- checkout: 왼쪽의 브랜치 메뉴에서 브랜치를 선택하고 더블 클릭하면 해당 브랜치로 돌아간다.


## git 연습사이트
 - [git 연습사이트][https://learngitbranching.js.org/?locale=ko]

## git 연습사이트 커맨드
- commit : 세이브, 스테이지 영역의 파일들을 가지고 커밋(=세이브)를 만들 수 있다.
- branch : 기존 내용을 유지한채 새로운 내용을 추가하고 싶을 때 사용
- checkout : 특정 브랜치(혹은 커밋) 으로 돌아가고 싶을 때 사용
- cherry-pick : 체리 한 바구니에서 제일 좋은 체리만 고르는 것에서 유래,
  -  git log에서 특정한 commit 하나만 콕 찝어서 현재 HEAD가 가리키는 branch에 추가
- reset
  - git reset --hard
    - reset 이후 push는 force 옵션 선택 필요
  - 이전 커밋은 사라짐
- revert
  - 쉽게 커밋을 되돌릴 수 있음구아우
  - reset과 유사하나 이전 커밋이 남아있음
  - 여러 커밋을 되돌리려면 최신부터 순서대로 revert를 반복해야함
- rebase
  - 리베이스도 병합(merge)과 마찬자기로 두 브랜치의 내용을 하나로 합치고 싶을 때 사용
- merge : 하나의 브랜치를 현재 브랜치와 합치는 것