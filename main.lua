Functions = require("Function")
os = require("os")
Table = require("List")

password = os.getenv("Password")

print("Input Name: ")
local Name = io.read()
print("Class: ")
local class = io.read()
print("Password: ")
local passwords = io.read()
if passwords == password then
  if Name == "DataBase" then
    os.execute("clear")
    for i,v in ipairs(Table.Students[class]) do
    print(i..".",v)
    Functions.sleep(.01)
  end
else
  for _, str in pairs(Table.Students[class]) do
  local PossibleName = nil
  if string.find(string.lower(str), string.lower(Name)) then
      os.execute("clear")
      PossibleName = str
      print(PossibleName)
    do return end
    end
end
end
else
  os.execute("clear")
  print("Password is wrong.")
end