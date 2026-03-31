age = int(input('请输入您的年龄：'))
has_report = input('您是否提交体检报告？（是/否）')
level = int(input('请输入您的会员等级（1/2/3）：'))

if 18 <= age <= 45:
    print('✅您的年龄符合参赛要求！')
    if has_report == '是':
        print('✅您已成功提交体检报告！')
        if level == 1:
            print(f'😊您是{level}级会员，赛后您可以领取纪念T恤👕一件！')
        elif level == 2:
            print(f'😊您是{level}级会员，赛后您可以领取专业跑鞋👟一双！')
        elif level == 3:
            print(f'😊您是{level}级会员，赛后您可以领取运动耳机🎧一副！')
        else:
            print('️您输入的会员等级有误！')
    elif has_report == '否':
        print('❌您未提交体检报告！无法参赛。')
    else:
        print('⚠️您未正确提交体检报告！')
else:
    print('❌参赛年龄需要在18~45之间！')
