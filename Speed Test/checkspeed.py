import speedtest
st = speedtest.Speedtest()
download = st.download()
upload = st.upload()

print("Download speed is: ", download)
print("Upload speed is: ", upload)

st.get_servers([])

ping = st.results.ping

print("Your Ping is: ", ping)