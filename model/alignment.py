import pandas as pd
import numpy as np
import sysi, time
import pickle

global_vocab = pd.read_csv("../global_vocab.csv", index_col="word_set")
print(global_vocab.head())

nw = len(global_vocab["count"]) # vocab size
#print(nw)
T = [i for i in range(0, 12)]  # 12 clusters
#print(T)

base_path = "../../reorganized_data/cluster"
save_path = "../../results"

def print_params(r, lam, tau, gam, emph, ITERS):
  print('rank = {}'.format(r))
  print('frob regularizer = {}'.format(lam))
  # finish later

if __name__ == '__main__':
  ITERS = 5 # total passes over data
  lam = 10  # frob regularizer
  gam = 100 # forcing regularizer
  tau = 50  # smoothing regulatizer
  r = 50    # rank
  b = nw    # batch size
  emph = 1  # emphasize the nonzero


  foo = sys.argv
  for i in range(1,len(foo)):
    if foo[i]=='-r':      r = int(float(foo[i+1]))
    if foo[i]=='-iters':  ITERS = int(float(foo[i+1]))
    if foo[i]=='-lam':    lam = float(foo[i+1])
    if foo[i]=='-tau':    tau = float(foo[i+1])
    if foo[i]=='-gam':    gam = float(foo[i+1])
    if foo[i]=='-b':      b = int(float(foo[i+1]))
    if foo[i]=='-emph':   emph = float(foo[i+1])
    if foo[i]=='-check':  erchk=foo[i+1]


  savefile = save_path+'L'+str(lam)+'T'+str(tau)+'G'+str(gam)+'A'+str(emph)

  print('starting training with following parameters')
  print_params(r, lam, tau, gam, emph, ITERS)
  print('there are a total of {} words, and {} time points'.format(nw, T))


  print("========================")
  print("initializing")

  # Ulist, Vlist are word embeddings created from svd from ppmi matrix at time T
  Ulist, Vlist = util.import_static_init(T) # to be implemented 

  print(Ulist.shape())
  print(Vlist.shape())

  print('getting batch indices')
  if b < nw:
    b_ind = util.getbatches(nw,b) # to be implemented
  else:
    b_ind = [range(nw)]

  start_time = time.time()
  
  # sequential updates
  for iteration in xrange(ITERS):
    print_params(r, lam, tau, gam, emph, ITERS)
    try:
      Ulist = pickle.load(open("%s_iter%d.p" % (savefile, iteration), "rb"))
      Vlist = pickle.load(open("%s_iter%d.p" % (savefale, iteration), "rb"))
      print('iteration {} loaded succesfully'.format(iteration))
      continue
    except(IOError):
      pass
    loss = 0

    # shuffle times ???
    # if iteration == 0: times = T
    # else: times = np.random.permutation(T)
    
    times = T
    for t in xrange(len(times)):
      print('iteration {}, time {}'.format(iteration, t))
      f = base_path + str(t) + '.csv'
      print(f)

      pmi = util.getgam(f, nw, False)
      for j in xrange(len(b_ind)):
        print('{} out of {}'.format(j. len(b_ind)))
        ind = b_ind[j]

        ## update V
        pmi_seg = pmi[:, ind].todense()

        if t==0:
          vp = np.zeros((len(ind),r))
          up = np.zeros((len(ind),r))
          iflag = True
        else:
          vp = Vlist[t-1][ind,:]
          up = Ulist[t-1][ind,:]
          iflag = False

        if t==len(T)-1:
          vn = np.zeros((len(ind),r))
          un = np.zeros((len(ind),r))
          iflag=True
        else:
          vn = Vlist[t+1][ind,:]
          un = Ulist[t+1][ind,:]
          iflag = False

        Vlist[t][ind,:] = util.update(Ulist[t], emph*pmi_seg, vp, vn, lam, tau, gam, ind, iflag)
        Ulist[t][ind,:] = util.update(Vlist[t], emph*pmi_seg, vp, vn, lam, tau, gam, ind, iflag)
    print('time elapsed = {}'.format(time.time()-start_time))

    pickle.dump(Ulist, open("%s_iters%d.p" % (savefile, iteration), "wb"), pickle.HIGHEST_PROTOCOL)
    pickle.dump(Vlist, open("%s_iters%d.p" % (savefile, iteration), "wb"), pickle.HIGHEST_PROTOCOL)


