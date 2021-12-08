import requests, io, http

fileID = "138pigzJ5q9JnNmySLYgikXX6dJkc-6Cg"
downloader = MediaIoBaseDownload(fh, request)

done = False
while done is False:
    status, done = downloader.next_chunk()
  #  print "Download %d%%." % int(status.progress() * 100)