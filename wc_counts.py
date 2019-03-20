

def wc_counts(file, n, l=5):
    print("loading",file)
    corp = load_corp("../dicts/"+file)
    print("loaded", file)
    wc = defaultdict(int)
    print("creaated wc, wnd")
    # increments values
    for tweet in corp:
        tweet = tweet.split()

        for i in range(len(tweet)):
            wc[tweet[i]]+=1

    wc = pd.DataFrame(wc, index=[0])
    wc = wc.T
    wc.to_csv("wc/wc" + str(n) + ".csv")

print("start")
path = "/opt/data/dicts"
dir_list = os.listdir(path)
for f, n in enumerate(dir_list):
    print(n, f)
    wc_counts(n, f)
