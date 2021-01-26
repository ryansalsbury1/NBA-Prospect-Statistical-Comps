#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 09:55:40 2020

@author: ryansalsbury
"""
############################# Totals ##################################
##### get season totals #####
pages = range(1,5)
years = range(2003,2021)
stat_dict={}
for year in years:
    for page_num in pages:
        url = "https://basketball.realgm.com/nba/stats/" + str(year) + "/Totals/Qualified/pts/All/desc/"+ str(page_num) + "/Regular_Season"
        page = urlopen(url).read()
        soup = BeautifulSoup(page)
        body = soup.find("tbody")
        if body != None:
            rows = body.find_all('tr')
        
            
        
            for row in rows:
                Player_ID = row.find("a").attrs['href'].split('/')[4]
                Player = row.findAll("td")[1].text
                Team = row.findAll("td")[2].text
                GP = row.findAll("td")[3].text
                MIN = row.findAll("td")[4].text
                FGM = row.findAll("td")[5].text
                FGA = row.findAll("td")[6].text
                FGpct = row.findAll("td")[7].text
                ThreePM = row.findAll("td")[8].text
                ThreePA = row.findAll("td")[9].text
                ThreePct = row.findAll("td")[10].text
                FTM = row.findAll("td")[11].text
                FTA = row.findAll("td")[12].text
                FTpct = row.findAll("td")[13].text
                TOV = row.findAll("td")[14].text
                PF = row.findAll("td")[15].text
                ORB = row.findAll("td")[16].text
                DRB = row.findAll("td")[17].text
                REB = row.findAll("td")[18].text
                AST = row.findAll("td")[19].text
                STL = row.findAll("td")[20].text
                BLK = row.findAll("td")[21].text
                PTS = row.findAll("td")[22].text
        
                if 'Player_ID' not in stat_dict.keys():
                    stat_dict['Player_ID'] = [Player_ID]  
                    stat_dict['Player'] = [Player]
                    stat_dict['Season'] = [year]
                    stat_dict['Team'] = [Team]
                    stat_dict['GP'] = [GP]
                    stat_dict['MIN'] = [MIN]
                    stat_dict['FGM'] = [FGM]
                    stat_dict['FGA'] = [FGA]
                    stat_dict['FGpct'] = [FGpct]
                    stat_dict['ThreePM'] = [ThreePM]
                    stat_dict['ThreePA'] = [ThreePA]
                    stat_dict['ThreePct'] = [ThreePct]
                    stat_dict['FTM'] = [FTM]
                    stat_dict['FTA'] = [FTA]
                    stat_dict['FTpct'] = [FTpct]
                    stat_dict['TOV'] = [TOV]
                    stat_dict['PF'] = [PF]
                    stat_dict['ORB'] = [ORB]
                    stat_dict['DRB'] = [DRB]
                    stat_dict['REB'] = [REB]
                    stat_dict['AST'] = [AST]
                    stat_dict['STL'] = [STL]
                    stat_dict['BLK'] = [BLK]
                    stat_dict['PTS'] = [PTS]
                    stat_dict['Type'] = ['Totals']
                else:  
                    stat_dict['Player_ID'].append(Player_ID)
                    stat_dict['Player'].append(Player)
                    stat_dict['Season'].append(year)
                    stat_dict['Team'].append(Team)
                    stat_dict['GP'].append(GP)
                    stat_dict['MIN'].append(MIN)
                    stat_dict['FGM'].append(FGM)
                    stat_dict['FGA'].append(FGA)
                    stat_dict['FGpct'].append(FGpct)
                    stat_dict['ThreePM'].append(ThreePM)
                    stat_dict['ThreePA'].append(ThreePA)
                    stat_dict['ThreePct'].append(ThreePct)
                    stat_dict['FTM'].append(FTM)
                    stat_dict['FTA'].append(FTA)
                    stat_dict['FTpct'].append(FTpct)
                    stat_dict['TOV'].append(TOV)
                    stat_dict['PF'].append(PF)
                    stat_dict['ORB'].append(ORB)
                    stat_dict['DRB'].append(DRB)
                    stat_dict['REB'].append(REB)
                    stat_dict['AST'].append(AST)
                    stat_dict['STL'].append(STL)
                    stat_dict['BLK'].append(BLK)
                    stat_dict['PTS'].append(PTS)
                    stat_dict['Type'].append('Totals')
        
nba_player_totals_2003_2020 = pd.DataFrame.from_dict(stat_dict)







############################# Misc ##################################
##### get season misc#####
page = range(1,5)
years = range(2003,2021)
stat_dict={}
for year in years:
    for page_num in pages:
        url = "https://basketball.realgm.com/nba/stats/" + str(year) + "/Misc/Qualified/WS/All/desc/"+ str(page_num) + "/Regular_Season"
        page = urlopen(url).read()
        soup = BeautifulSoup(page)
        body = soup.find("tbody")
        if body != None:
            rows = body.find_all('tr')
        
        
            for row in rows:
                Player_ID = row.find("a").attrs['href'].split('/')[4]
                Player = row.findAll("td")[1].text
                Team = row.findAll("td")[2].text
                DblDbl = row.findAll("td")[3].text
                TplDbl = row.findAll("td")[4].text
                FortyPts = row.findAll("td")[5].text
                TwentyReb = row.findAll("td")[6].text
                TwentyAst = row.findAll("td")[7].text
                FiveStl = row.findAll("td")[8].text
                FiveBlk = row.findAll("td")[9].text
                HighGame = row.findAll("td")[10].text
                Techs = row.findAll("td")[11].text
                HOB = row.findAll("td")[12].text
                AstTO = row.findAll("td")[13].text
                StlTO = row.findAll("td")[14].text
                FTFGA = row.findAll("td")[15].text
                Ws = row.findAll("td")[16].text
                Ls = row.findAll("td")[17].text
                WinPct = row.findAll("td")[18].text
                OWS = row.findAll("td")[19].text
                DWS = row.findAll("td")[20].text
                WS = row.findAll("td")[21].text

        
                if 'Player_ID' not in stat_dict.keys():
                    stat_dict['Player_ID'] = [Player_ID]  
                    stat_dict['Player'] = [Player]
                    stat_dict['Season'] = [year]
                    stat_dict['Team'] = [Team]
                    stat_dict['DblDbl'] = [DblDbl]
                    stat_dict['TplDbl'] = [TplDbl]
                    stat_dict['FortyPts'] = [FortyPts]
                    stat_dict['TwentyReb'] = [TwentyReb]
                    stat_dict['TwentyAst'] = [TwentyAst]
                    stat_dict['FiveStl'] = [FiveStl]
                    stat_dict['FiveBlk'] = [FiveBlk]
                    stat_dict['HighGame'] = [HighGame]
                    stat_dict['Techs'] = [Techs]
                    stat_dict['HOB'] = [HOB]
                    stat_dict['AstTO'] = [AstTO]
                    stat_dict['StlTO'] = [StlTO]
                    stat_dict['FTFGA'] = [FTFGA]
                    stat_dict['Ws'] = [Ws]
                    stat_dict['Ls'] = [Ls]
                    stat_dict['WinPct'] = [WinPct]
                    stat_dict['OWS'] = [OWS]
                    stat_dict['DWS'] = [DWS]
                    stat_dict['WS'] = [WS]
                    stat_dict['Type'] = ['Misc']
                else:  
                    stat_dict['Player_ID'].append(Player_ID)
                    stat_dict['Player'].append(Player)
                    stat_dict['Season'].append(year)
                    stat_dict['Team'].append(Team)
                    stat_dict['DblDbl'].append(DblDbl)
                    stat_dict['TplDbl'].append(TplDbl)
                    stat_dict['FortyPts'].append(FortyPts)
                    stat_dict['TwentyReb'].append(TwentyReb)
                    stat_dict['TwentyAst'].append(TwentyAst)
                    stat_dict['FiveStl'].append(FiveStl)
                    stat_dict['FiveBlk'].append(FiveBlk)
                    stat_dict['HighGame'].append(HighGame)
                    stat_dict['Techs'].append(Techs)
                    stat_dict['HOB'].append(HOB)
                    stat_dict['AstTO'].append(AstTO)
                    stat_dict['StlTO'].append(StlTO)
                    stat_dict['FTFGA'].append(FTFGA)
                    stat_dict['Ws'].append(Ws)
                    stat_dict['Ls'].append(Ls)
                    stat_dict['WinPct'].append(WinPct)
                    stat_dict['OWS'].append(OWS)
                    stat_dict['DWS'].append(DWS)
                    stat_dict['WS'].append(WS)
                    stat_dict['Type'].append('Misc')

nba_player_misc_2003_2020 = pd.DataFrame.from_dict(stat_dict)




page = range(1,5)
years = range(2003,2021)
stat_dict={}
for year in years:
    for page_num in pages:
        url = "https://basketball.realgm.com/nba/stats/" + str(year) + "/Advanced_Stats/Qualified/per/All/desc/"+ str(page_num) + "/Regular_Season"
        page = urlopen(url).read()
        soup = BeautifulSoup(page)
        body = soup.find("tbody")
        if body != None:
            rows = body.find_all('tr')
        
        
            for row in rows:
                Player_ID = row.find("a").attrs['href'].split('/')[4]
                Player = row.findAll("td")[1].text
                Team = row.findAll("td")[2].text
                TSpct = row.findAll("td")[3].text
                eFGpct = row.findAll("td")[4].text
                TotalSpct = row.findAll("td")[5].text
                ORBpct = row.findAll("td")[6].text
                DRBpct = row.findAll("td")[7].text
                TRBpct = row.findAll("td")[8].text
                ASTpct = row.findAll("td")[9].text
                TOVpct = row.findAll("td")[10].text
                STLpct = row.findAll("td")[11].text
                BLKpct = row.findAll("td")[12].text
                USGpct = row.findAll("td")[13].text
                PPR = row.findAll("td")[14].text
                PPS = row.findAll("td")[15].text
                ORtg = row.findAll("td")[16].text
                DRtg = row.findAll("td")[17].text
                eDiff = row.findAll("td")[18].text
                FIC = row.findAll("td")[19].text
                PER = row.findAll("td")[20].text

        
                if 'Player_ID' not in stat_dict.keys():
                    stat_dict['Player_ID'] = [Player_ID]  
                    stat_dict['Player'] = [Player]
                    stat_dict['Season'] = [year]
                    stat_dict['Team'] = [Team]
                    stat_dict['TSpct'] = [TSpct]
                    stat_dict['eFGpct'] = [eFGpct]
                    stat_dict['TotalSpct'] = [TotalSpct]
                    stat_dict['ORBpct'] = [ORBpct]
                    stat_dict['DRBpct'] = [DRBpct]
                    stat_dict['TRBpct'] = [TRBpct]
                    stat_dict['ASTpct'] = [ASTpct]
                    stat_dict['TOVpct'] = [TOVpct]
                    stat_dict['STLpct'] = [STLpct]
                    stat_dict['BLKpct'] = [BLKpct]
                    stat_dict['USGpct'] = [USGpct]
                    stat_dict['PPR'] = [PPR]
                    stat_dict['PPS'] = [PPS]
                    stat_dict['ORtg'] = [ORtg]
                    stat_dict['DRtg'] = [DRtg]
                    stat_dict['eDiff'] = [eDiff]
                    stat_dict['FIC'] = [FIC]
                    stat_dict['PER'] = [PER]
                    stat_dict['Type'] = ['Advanced']
                else:  
                    stat_dict['Player_ID'].append(Player_ID)
                    stat_dict['Player'].append(Player)
                    stat_dict['Season'].append(year)
                    stat_dict['Team'].append(Team)
                    stat_dict['TSpct'].append(TSpct)
                    stat_dict['eFGpct'].append(eFGpct)
                    stat_dict['TotalSpct'].append(TotalSpct)
                    stat_dict['ORBpct'].append(ORBpct)
                    stat_dict['DRBpct'].append(DRBpct)
                    stat_dict['TRBpct'].append(TRBpct)
                    stat_dict['ASTpct'].append(ASTpct)
                    stat_dict['TOVpct'].append(TOVpct)
                    stat_dict['STLpct'].append(STLpct)
                    stat_dict['BLKpct'].append(BLKpct)
                    stat_dict['USGpct'].append(USGpct)
                    stat_dict['PPR'].append(PPR)
                    stat_dict['PPS'].append(PPS)
                    stat_dict['ORtg'].append(ORtg)
                    stat_dict['DRtg'].append(DRtg)
                    stat_dict['eDiff'].append(eDiff)
                    stat_dict['FIC'].append(FIC)
                    stat_dict['PER'].append(PER)
                    stat_dict['Type'].append('Advanced')

nba_player_advanced_2003_2020 = pd.DataFrame.from_dict(stat_dict)


##### write to csv #####
nba_player_totals_2003_2020.to_csv("nba_player_totals_2003_2020.csv", index=False)
nba_player_misc_2003_2020.to_csv("nba_player_misc_2003_2020.csv", index=False)
nba_player_advanced_2003_2020.to_csv("nba_player_advanced_2003_2020.csv", index=False)
