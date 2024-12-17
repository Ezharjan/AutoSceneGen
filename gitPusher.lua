local branchName = "master"


local function commander(argToExcute)
    local result = io.popen(argToExcute)
    local strInfo = result:read("*all")
    return strInfo
end

function tryTillSucceed(arg, tryTimes)
    tryTimes = tryTimes or 1000
    for i = 1, tryTimes, 1 do
        print("argument is: ", arg)
        local res = commander(arg)
        if res ~= "" then
            print("Conduction succeeded!")
            break
        end
    end
end

-- local curTime = os.date("%c")
local curTime = os.date("%Y-%m-%d %H:%M:%S")
print(curTime)
local cmds = {
    "git pull",
    "git add .",
    ("git commit -m \"%s"):format(tostring(curTime)) .. "\"",
    "git push -u origin " .. branchName,
    "git pull"
}

local pushMaster2github = "git push -u origin " .. branchName
local pull = "git pull"
for i = 1, #cmds, 1 do
    print(("running `%s`"):format(cmds[i]))
    commander(cmds[i])
end
tryTillSucceed(pull)
tryTillSucceed(pushMaster2github)
