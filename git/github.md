# Github
{id: github}


## Fork repository
{id: fork-repository}

* Visit [particpants](https://github.com/collab-dev/participants)
* fork


## Forking workflow
{id: forking-workflow}

* Joe has a local and a remote repository.  https://github.com/joe/demo
* Mary "fork" the repository of Joe creating a remote copy of her own: https://github.com/mary/demo
* Mary clones her remote repository to the local disk
* Mary creates a local branch called 'feature', makes some changes, pushes the changes out to the 'feature' branch in her own remote repo.
* Mary sends a "pull request" to Joe asking Joe to integrate the changes to the master branch of his own repository.
* If Joe has comments, he makes them. Mary can make further changes in the 'feature' branch, and push them out.
* Once Joe is satisfied with the pull-request he accepts it merging the changes to his own "master" branch.
* Mary sets up the remote repository of Joe to be a remote repository of her own. (She only needs to do this once per repo.) git remote add upstream https://github.com/joe/demo.git
* Mary changes to "master" locally, and pulls from Joe: **git checkout master** **git pull upstream master**
* Mary can then delete the local and remote 'feature' branch.
* If Mary already has other  feature branchese she might want to rebase them onto "master" so they will be based on the most recent changes.



## Clone a repository from Github
{id: clone-from-github}
{i: clone}


Let's see [GithuGithubb](https://github.com/)


```
$ git clone git://github.com/eilara/camel-defense.git
```

```
git remote -v

origin	https://github.com/cm-demo/participants (fetch)
origin	https://github.com/cm-demo/participants (push)
```


## Github fork
{id: github-fork}


Forking on Github will create another copy of the public repository, but in your own user-space.
You then clone from that place. Make changes locally, commit them and push them to your own public repository.




Integration: You can send a `pull request` to the author via the Github web site.
He can then either merge your changes on the Github site or can do it on his local machine.




## git remote add
{id: git-remote-add}
{i: remote}

```
$ git remote
origin

$ git remote add upstream /path/to/git/repo2
$ git remote
origin
upstream


$ git pull

$ git fetch upstream
$ git merge upstream/master
```



## Public key
{id: public-key}


[Generating SSH Keys](https://help.github.com/articles/generating-ssh-keys) and add them to a Github account


## Exercise
{id: exercise-github}

* Clone [this repository](http://github.com/szabgab/git-201303005) from Github and check its history
* Create an account on Github
* Fork a repository and clone it.
* Make some changes: create a file your_git_user.txt
* push the changes to Github
* Observer the changes have arrived
* Send a pull request

* Find other people in the team who have forked the project.
* Set up the repository of one of them as remote.
* Fetch and merge their changes.


## Make some local changes
{id: make-some-local-changes}

```
git checkout -b feature
   edit participants.json file
git add participants.json
git commit -m "some change"
```

## push out local changes to branch
{id: pus-out-local-changes-to-branch}

```
git push

fatal: The current branch feature has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin feature
```

```
$  git push -u origin feature

Total 0 (delta 0), reused 0 (delta 0)
To github.com:collab-dev/participants/
 * [new branch]      feature -> feature
Branch 'feature' set up to track remote branch 'feature' from 'origin'.
```

## Send Pull-Request
{id: send-pull-request}

* Visit [particpants](https://github.com/collab-dev/participants)

## Make more changes and update the pull-request
{id: update-pull-request}

```
git add .
git commit
git push
```

* Visit [particpants](https://github.com/collab-dev/participants)


## Follow the changes in the original repository
{id: follow-changes}


```
git remote add upstream https://github.com/collab-dev/participants.git
git checkout master
git pull upstream master
git push
```

## Remove local branch
{id: remove-local-branch}

```
git checkout maste
git branch -d feature
```

## Remove remote branch
{id: remove-remote-branch}


```
$  git push origin :feature

To github.com:collab-dev/participants/
 - [deleted]         feature
```





