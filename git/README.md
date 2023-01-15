# 2023 AWS Cloud Bootcamp "Git 사례공유"

# Git을 왜 사용해야 하는가?
현재 사용되는 형상관리툴
- Client/Server 타입 : Subversion(SVN), CVS, Perforce, ClearCase, TFS
- 분산저장소 타입 : Git, Mercurial, Bitkeeper, SVK, Darcs
- Folder 공유 타입 : RCS, SCCS

가장 많이 사용하는 툴 : SVN, Git

4. SVN vs GIT 비교

- 특징

4.1 SVN
 - SVN은 보통 대부분의 기능을 완성해놓고 소스를 중앙 저장소에 commit
 - commit의 이미 자체가 중앙 저장소에 해당 기능을 공개한다는 의미.
 - (GIT 과 가장 큰 차이점) 개발자가 자신만의 version history를 가질 수 없다. (그렇기 때문에 local History를 이용하긴 하지만, 일시적이다. 내가 몇일전 까지에 한하여 작업했던 내역을 확인 가능하지만 버전 관리가 되진 않는다.)
 - commit한 내용에 실수가 있을 시에 다른 개발자에게 바로 영향을 미치게 되는 단점도 있다.

4.2 GIT
 - (GIT 과 가장 큰 차이점) 반면, git은 개발자가 자신만의 commit history를 가질 수 있고, 개발자와 서버의 저장소는 독립적으로 관리가 가능.
 - commit한 내용에 실수가 있더라도 이 바로 서버에 영향을 미치지 않는다
 - 개발자는 마음대로 commit(push)하다가 자신이 원하는 순간에 서버에 변경 내역(commit history)을 보낼 수 있으며, 서버의 통합 관리자는 관리자가 원하는 순간에 각 개발자의 commit history를 가져올 수 있음.

이렇게 git은 서버 저장소와 개발자 저장소가 독립적으로 commit history를 가져갈 수 있기 때문에 매우 유연한 방식으로 소스를 운영할 수 있으며, 이러한 유연성이 git의 가장 큰 장점이다.

형상관리(Configuration Management)란?

버전관리(Version Management)라고도 한다.
각자가 개발한 코드/문서들을 하나의 관리 도구에서 통합적으로 버전별로 관리하게 되는 것
크게 중앙집중식과 분산관리식으로 나뉘며
대표적으로 사용되는 도구는 중앙집중식의 SVN 그리고 분산관리식의 git 이다.
SVN, git 비교

1) SVN (Subversion)

로컬 PC에서 commit하면 중앙 저장소에 반영
장점 : 직관적이라 쉬움
단점 : 충돌 확률 높음, 에러 시 복구 어려움
2) git

로컬 PC에서 commit하면 로컬 저장소에 반영되고 로컬저장소에서 push하면 원격 저장소에 반영
장점 : 처리속도 빠름, 웹 상의 저장소, 협업 용이성, 에러 시 복구 용이
단점 : 직관적이지 못함 (공유 과정이 비교적 복잡, 이는 상대적인 것으로 git에 대해 GUI 제공해주는 github desktop 등을 사용하면 어렵지 않음!)

git 특징

git은 모든 변경사항과 파일들을 모든 시점에서 트래킹(추적)한다.
- 무엇이, 어디에서, 언제, 누구에 의해 바뀌었는지 등을 알 수 있음
- 파일 수정 중에 실수로 웹 사이트가 망가졌다면, 이전 시점으로 되돌아갈 수 있게 함
git은 0,1로 이루어진 binary code로 파일을 읽기 때문에 원하는 것이 무엇이든 읽을 수 있다. (오디오, 이미지, 엑셀파일, 텍스트파일 등도 가능)
git github 차이

git은 소스코드를 효과적으로 관리할 수 있게 해주는 소프트웨어 그 자체.
github는 나의 git 파일을 업로드하는 곳. git의 웹호스팅을 제공 (github 말고도 gitlab, bitbucket 등이 있음)
github로 인해 변경사항을 회사, 칭구와 공유할 수 있음. 나의 git 파일 업로드, 다른 사람의 git 파일 다운로드 가능. (git ≠ github)
github desktop은 가독성이 좋지 않은 CLI(Command Line Interface)의 git을 위해 보기 좋게 GUI(Graphic User Interface)를 제공해주는 프로그램
따라서 이력서에 github가 아닌 git을 할 줄 안다고 적어야겠다.

원격 저장소 (Remote Repository)
로컬 저장소 (Local Repository)
클론 (Clone)
작업 디렉토리 (Working Directory)
스테이징 영역 (Staging Area)
커밋 (Commit)
 
그러면 각각의 용어에 대해서 알아보겠습니다.

본인이 수행한 부분이 어디인지를 구체적으로 파악하고 코딩 스타일을 체크하기 위해 포트폴리오를 요구하는 경우도 많은데요. 포트폴리오를 준비할 때 이를 활용한다면 본인의 프로그래밍 실력을 더욱 투명하고 직관적으로 어필할 수 있어 구직활동에 큰 도움이 됩니다. 