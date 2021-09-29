function Initialize()
	size = SKIN:GetVariable('size', '90')
    groupName = SKIN:GetVariable('groupName')

    minScale = SKIN:GetVariable('minScale', '1')
    maxScale = SKIN:GetVariable('maxScale', '1')

    minOffsetX = SKIN:GetVariable('minOffsetX', '0')
    maxOffsetX = SKIN:GetVariable('maxOffsetX', '0')
    minOffsetY = SKIN:GetVariable('minOffsetY', '0')
    maxOffsetY = SKIN:GetVariable('maxOffsetY', '0')
end

function RunBangs(tableOfBangs)
    for _, v in next,tableOfBangs,nil do
        SKIN:Bang(v)
    end
end

function Toggle()
    if SKIN:GetVariable('maximized', '0') == '0' then
        Maximize()
    else
        Minimize()
    end
end

function Maximize()
    RunBangs({
        '!SetVariable maximized 1',
        '!SetVariable curScale ' .. minScale,
        '!ShowMeter Frame',
        '!ShowGroup ' .. groupName,
        '!SetVariable curOffsetX ' .. maxOffsetX,
        '!SetVariable curOffsetY ' .. maxOffsetY,
        '!Redraw'
    })
end

function Minimize()
    RunBangs({
        '!SetVariable maximized 0',
        '!SetVariable curScale ' .. maxScale,
        '!SetVariable curOffsetX ' .. minOffsetX,
        '!SetVariable curOffsetY ' .. minOffsetY,
        '!HideMeter Frame',
        '!HideGroup ' .. groupName,
        '!Redraw'
    })
end