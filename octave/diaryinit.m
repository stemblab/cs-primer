function diaryinit(fname)

  if exist(fname,'file') == 2; delete(fname); end
  diary(fname);diary off

