local lunatest = require "lunatest"
local bit32 = require "bit32"

function convert_tb_binary(tb)
	for i=1, #tb do
		tb[i] = tonumber(tb[i])
		--cannot found to binary method.... 
	end
	return tb
end

function lua_string_split(str, split_char)
    local sub_str_tab = {};
    for mu_id in string.gmatch(str, "(%d+)|*") do
        table.insert(sub_str_tab, mu_id)
    end
    return convert_tb_binary(sub_str_tab);
end

function generate_mask(array)
	print("start")
	for i= 1, #array do
		local tptb = lua_string_split(array[i])
		print("--------------")
		print_tb(tptb)
	end

end

function print_tb(tb)
	for i=1, #tb do
		print(tb[i])
	end
end

function test_assert_false()
   source = {"194.85.160.177", "194.85.160.183", "194.85.160.178"}
   generate_mask(source)
   lunatest.assert_false(false)
end

lunatest.run()
