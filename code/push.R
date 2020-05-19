git2r::add(path = ".")
git2r::commit(message = "build gitbook")
git2r::push(name = 'origin', refspec = "refs/heads/master", cred = git2r::cred_token())
