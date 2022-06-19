import git 

g = git.cmd.Git("https://github.com/RDEG1/test2.git")
# g.commit('about12.html')
# g.commit("mypythontest")
g.pull()