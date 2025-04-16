choice1 = make_slide("salem_1692.jpg", "Salem, 1692: Your neighbor's pigs died after your argument. You're accused of witchcraft. First move:", ["Deny", "False confession", "Stay silent", ""], a=.15, b=.15)

match choice1:
    case "Deny":
        choice2 = make_slide("mccarthy.jpg", "1953 court case: You deny all the accusations. 'Only guilty people deny!' the council says. Next move:", ["Ask for lawyer", "Plead Fifth", "Name peers", "Accuse council"], a=1.15, b=1.15)
        match choice2:
            case "Ask for lawyer":
                choice3 = make_slide("salem_1692.jpg", "Salem: The judge yells 'Devil's agents do not need defense!' Final move:", ["Quote Bible", "Curse the court", "Say you're pregnant", "Claim accusers are witches"], a=.15, b=.15)
                match choice3:
                    case "Quote Bible": make_slide("mccarthy.jpg", "1953 Outcome: Cited for contempt. Blacklisted. Can't find work for decades.", a=1.15, b=1.15)
                    case "Curse the court": make_slide("mccarthy.jpg", "1953 Outcome: Declared mentally unstable. Confined to asylum 'rehabilitation'.", a=1.15, b=1.15)
                    case "Say you're pregnant": make_slide("mccarthy.jpg", "1953 Outcome: Put under FBI surveillance until 'proof' emerges.", a=1.15, b=1.15)
                    case "Claim accusers are witches": make_slide("mccarthy.jpg", "1953 Outcome: Countersuit backfires. labeled 'agitator.' Passport revoked.", a=1.15, b=1.15)
            case "Plead Fifth":
                choice3 = make_slide("salem_1692.jpg", "Salem: They say the devil has stopped you from speaking so they try to test your fate. Next move:", ["Say a prayer", "Stay silent", "Fake possession", "False confession"], a=.15, b=.15)
                match choice3:
                    case "Say a prayer": make_slide("mccarthy.jpg", "1953 Outcome: Career over, house vandalized.", a=1.15, b=1.15)
                    case "Stay silent": make_slide("mccarthy.jpg", "1953 Outcome: Expelled from union. Can't work legally again.", a=1.15, b=1.15)
                    case "Fake possession": make_slide("mccarthy.jpg", "1953 Outcome: Committed for CIA anti-communist experiments.", a=1.15, b=1.15)
                    case "False confession": make_slide("mccarthy.jpg", "1953 Outcome: Become informant naming old friends.", a=1.15, b=1.15)
            case "Name peers":
                choice3 = make_slide("salem_1692.jpg", "Salem: You name others. They demand evidence. Next move:", ["Bring poppet", "Point at shadow", "Cry", "Refuse"], a=.15, b=.15)
                match choice3:
                    case "Bring poppet": make_slide("mccarthy.jpg", "1953 Outcome: Possibly forged letters turn up and 'prove' your claims. Keep your job.", a=1.15, b=1.15)
                    case "Point at shadow": make_slide("mccarthy.jpg", "1953 Outcome: Your accusations spark office purges. Promoted because fear.", a=1.15, b=1.15)
                    case "Cry": make_slide("mccarthy.jpg", "1953 Outcome: Hailed as hero and patriot. Forced to testify at 28 hearings.", a=1.15, b=1.15)
                    case "Refuse": make_slide("mccarthy.jpg", "1953 Outcome: Marked 'unreliable.' Lose your job.", a=1.15, b=1.15)
            case "Accuse council":
                choice3 = make_slide("salem_1692.jpg", "Salem: You accuse the judge of witchcraft. Chaos erupts. Final move:", ["Present 'proof'", "Flee", "", ""], a=.15, b=.15)
                match choice3:
                    case "Present 'proof'": make_slide("mccarthy.jpg", "1953 Outcome: Found guilty of perjury.", a=1.15, b=1.15)
                    case "Flee": make_slide("mccarthy.jpg", "1953 Outcome: Escape to Mexico. Communist rumors follows you.", a=1.15, b=1.15)

    case "False confession":
        choice2 = make_slide("mccarthy.jpg", "1953: You admit past Party ties to save career and name some of your peers. The council demands proof:", ["Bring poppet", "Point at shadow", "Cry", "Refuse"], a=1.15, b=1.15)
        match choice2:
            case "Bring poppet": make_slide("mccarthy.jpg", "1953 Outcome: Possibly forged letters turn up and 'prove' your claims. Keep your job.", a=1.15, b=1.15)
            case "Point at shadow": make_slide("mccarthy.jpg", "1953 Outcome: Your accusations spark office purges. Promoted because fear.", a=1.15, b=1.15)
            case "Cry": make_slide("mccarthy.jpg", "1953 Outcome: Hailed as hero and patriot. Forced to testify at 28 hearings.", a=1.15, b=1.15)
            case "Refuse": make_slide("mccarthy.jpg", "1953 Outcome: Marked 'unreliable.' Lose your job.", a=1.15, b=1.15)
    case "Stay silent":
        choice2 = make_slide("mccarthy.jpg", "1953: You invoke the Fifth Amendment. The committee threatens you and your friends' careers.", ["Testify to protect them", "Stay silent", "Demand defense", ""], a=1.15, b=1.15)
        match choice2:
            case "Testify to protect them":
                choice3 = make_slide("salem_1692.jpg", "Salem: To save your friends, you speak — but your voice cracks. The crowd becomes even MORE suspicuous.", ["Blame the Devil", "Claim illness", "Collapse", ""], a=.15, b=.15)
                match choice3:
                    case "Blame the Devil": make_slide("mccarthy.jpg", "1953 Outcome: They say you've been 'brainwashed.' Forced into CIA anti-communist experiments", a=1.15, b=1.15)
                    case "Claim illness": make_slide("mccarthy.jpg", "1953 Outcome: Called a security risk. Fired, medical help denied.", a=1.15, b=1.15)
                    case "Collapse": make_slide("mccarthy.jpg", "1953 Outcome: Weakness is guilt! Become social outcast.", a=1.15, b=1.15)
            case "Stay silent":
                choice3 = make_slide("salem_1692.jpg", "Salem: You rot in jail. The council offers one last deal: confess or hang.", ["Confess falsely", "Stay defiant", "Bribe guard", "Write confession"], a=.15, b=.15)
                match choice3:
                    case "Confess falsely": make_slide("mccarthy.jpg", "1953 Outcome: Forced to confess on radio. Still added to Hollywood blacklist.", a=1.15, b=1.15)
                    case "Stay defiant": make_slide("mccarthy.jpg", "1953 Outcome: Guilty for contempt of court. Sent to federal prison for sedition.", a=1.15, b=1.15)
                    case "Bribe guard": make_slide("mccarthy.jpg", "1953 Outcome: Bribe discovered. Sent to prison.", a=1.15, b=1.15)
                    case "Write confession": make_slide("mccarthy.jpg", "1953 Outcome: Confession becomes bestseller. You're rich!", a=1.15, b=1.15)
            case "Demand defense":
                choice3 = make_slide("salem_1692.jpg", "Salem: 'Lawyers defend only the guilty!' they shout. Final choice:", ["Quote law", "Insist on rights", "Attack the judge", "Apologize"], a=.15, b=.15)
                match choice3:
                    case "Quote English law": make_slide("mccarthy.jpg", "1953 Outcome: Foreign influence accusation. Citizenship taken away.", a=1.15, b=1.15)
                    case "Insist on rights": make_slide("mccarthy.jpg", "1953 Outcome: Rights = Communism, Jailed without trial for 2 years.", a=1.15, b=1.15)
                    case "Attack the judge": make_slide("mccarthy.jpg", "1953 Outcome: Beaten for resisting arrest. Left crippled, unemployed.", a=1.15, b=1.15)
                    case "Apologize": make_slide("mccarthy.jpg", "1953 Outcome: Apology aired on radio. Hired as McCarthy's janitor.", a=1.15, b=1.15)

