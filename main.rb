def del_file(file)
  system("if exist "+file+" del "+file)
end

def get_names(file_data, names)
  sub_str = "All User Profile" 
  for i in 0...file_data.length
    if file_data[i].include? sub_str
      names.append((file_data[i])[27...file_data[i].length])
    end
  end
end

def get_password(pass_data)
  sub_str = "Key Content"
  for i in 0...pass_data.length
    if pass_data[i].include? sub_str
      return (pass_data[i])[29...pass_data[i].length]
    end
  end
  return "No password found"
end

password = []

del_file "file.txt"
system("netsh wlan show profile > file.txt")
file_file = File.open("file.txt")
file_data = file_file.readlines.map(&:chomp)
names = []
get_names file_data, names
for i in 0...names.length
  name = names[i]
  del_file "passwd.txt"
  system("netsh wlan show profile "+name+" key=clear > passwd.txt")
  pass_file = File.open("passwd.txt")
  pass_data = pass_file.readlines.map(&:chomp)
  password.append(get_password pass_data)
  pass_file.close
end
file_file.close
result = ""
for i in 0...password.length
  result += names[i]+": "+password[i]+"\n"
end
del_file "passwd.txt"
system("type nul > passwd.txt")
passwd_file = File.open("passwd.txt", "w")
passwd_file.write(result)