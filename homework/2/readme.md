Homework 2: Advanced Git  
A.
```bash
$ git branch test1
$ git branch test2
```  
B.
```bash
$ git checkout test1
Switched to branch `test1`
$ touch test.txt
```  
C.
```bash
$ echo "This is some example test for branch test1" >> test.txt
```  
D.
```bash
$ git add -A
$ git commit -a -m "Stage D of homework 2"
[test1 c0f67aa] Stage D of homework 2
 1 file changed, 1 insertion(+)
 create mode 100644 homework/2/test.txt
```  
E.
```bash
$ git checkout test2
Switched to branch 'test2'
$ ls
readme.md
```  
The lack of test.txt in homework/2/ is because git automatically adds, removes or  
edits files so that they're synced with what the branches most recent commit. Because  
test2 didn't have the test.txt in it when the branch was created the file was deleted  
to match the last commit of master.
F.
```bash
$ touch test.txt
$ echo "This is some example test for branch test2" >> test.txt
```  
G.
```bash
$ git checkout test1
error: The following untracked working tree files would be overwritten by checkout:
	homework/2/test.txt
Please move or remove them before you can switch branches.
Aborting
$ git add -A
$ git commit -a -m "Stage F of homework 2"
[test2 85b9678] Stage F of homework 2
 1 file changed, 1 insertion(+)
 create mode 100644 homework/2/test.txt
$ git checkout test1
Switched to branch 'test1'
```  
H.
```bash
$ git checkout master
Switched to branch 'master'
Your branch is up-to-date with 'origin/master'.
$ git merge test1
Updating 357573f..c0f67aa
Fast-forward
 homework/2/test.txt | 1 +
 1 file changed, 1 insertion(+)
 create mode 100644 homework/2/test.txt
```  
I.
```bash
$ ls
readme.md test.txt
```  
I see readme.md and the test.txt from the test1 branch  
J.
```bash
$ git merge test2
Auto-merging homework/2/test.txt
CONFLICT (add/add): Merge conflict in homework/2/test.txt
Automatic merge failed; fix conflicts and then commit the result.
```  
I get a merge conflict trying to bring a new test.txt into master when there is already  
an existing version there. This is because both files are different and git needs me to  
fix the conflict before merging.  
K.
```bash
$ git checkout test2
homework/2/test.txt: needs merge
error: you need to resolve your current index first
```  
Error is saying that were need to fix the merge to master before I can do anything else.
L.
```bash
$ git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)
You have unmerged paths.
  (fix conflicts and run "git commit")

Unmerged paths:
  (use "git add <file>..." to mark resolution)

	both added:      test.txt

no changes added to commit (use "git add" and/or "git commit -a")

```  
There's unmerged paths, meaning that the two test.txt files never actually merged because  
the contents of both files are different and git needs me to resolve the conflict.  
M.
```bash
$ vim test.txt
```  
vim opened the document, I changed it so the only thing in the .txt was "." and then exited  
by pressing ESC and typing ":wq".
N.
```bash
$ git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)
You have unmerged paths.
  (fix conflicts and run "git commit")

Unmerged paths:
  (use "git add <file>..." to mark resolution)

	both added:      test.txt

no changes added to commit (use "git add" and/or "git commit -a")
$ git add -A
$ git commit -a -m "Stage N of homework 2"
[master fe5bce1] Stage N of homework 2
```  
O.
```bash
$ git checkout test2
Switched to branch 'test2'
$ git branch -d test1
error: The branch 'test1' is not fully merged.
If you are sure you want to delete it, run 'git branch -D test1'.
```  
I get an error stating that test1 isn't yet fully merged into master.  
P.
```bash
$ git checkout master
Switched to branch 'master'
Your branch is ahead of 'origin/master' by 3 commits.
  (use "git push" to publish your local commits)
$ git branch -d test1
Deleted branch test1 (was c0f67aa).
$ git branch
* master
  test2
```  
We get a message saying that the test1 branch was deleted.
Q.
Because you're only allowed to delete braches that need to be merged from branches that do  
not need to be merged. Because test1 and test2 both need to be merged, neither can be deleted  
from the other.  
R.
```bash
$ git checkout test2
Switched to branch 'test2'
$ git branch -d test2
error: Cannot delete the branch 'test2' which you are currently on.
```  
Given an error stating that I cannot delete a branch because I am currently on it.  
S.
```bash
$ git checkout master
Switched to branch 'master'
Your branch is ahead of 'origin/master' by 3 commits.
  (use "git push" to publish your local commits)
$ git branch -d test2
Deleted branch test2 (was 85b9678).
$ git branch
* master
```  
T.
```bash
$ git add -A
$ git commit -a -m "Completing homework 2"
[master fbe612b] Completing homework 2
 1 file changed, 185 insertions(+), 2 deletions(-)
 rewrite homework/2/readme.md (96%)
$ git push
Counting objects: 20, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (17/17), done.
Writing objects: 100% (20/20), 3.20 KiB | 0 bytes/s, done.
Total 20 (delta 5), reused 0 (delta 0)
remote: Resolving deltas: 100% (5/5), completed with 1 local objects.
To git@github.com:ChristianG21/ECL2017S.git
   357573f..fbe612b  master -> master
```  
