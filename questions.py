# replace all outcomes with trying to get the player to predict the corresponding outcome for the 50s.
# replace all images of 1600s with the salem_1692 and 1950s with mccarthy
choice1 = make_slide("salem_1692.jpg", "Salem, 1692: Your neighbor's pigs died after your argument. You're accused of witchcraft. What do you do?", ["Deny", "False confession", "Stay silent", "Blame someone else"], a=.25, b=.25)

match choice1:
    case "Deny":
        choice2 = make_slide("mccarthy.jpg", "1953 HUAC Hearing: You deny communist ties. 'Only the guilty refuse names,' they say. Next move?", ["Demand lawyer", "Plead Fifth", "Name colleagues", "Accuse committee"], a=1.25, b=1.25)
        match choice2:
            case "Demand lawyer":
                choice3 = make_slide("salem_court.jpg", "Salem: The magistrate laughs. 'Devil's agents need no counsel!' Final plea?", ["Quote Scripture", "Curse the court", "Claim pregnancy", "Name accusers"])
                match choice3:
                    case "Quote Scripture": make_slide("mccarthy.jpg", "1950s Outcome: Cited for contempt. Blacklisted. Can't find work for decades.", a=1.25, b=1.25)
                    case "Curse the court": make_slide("mccarthy.jpg", "1950s Outcome: Declared mentally unstable. Confined to asylum 'rehabilitation'.", a=1.25, b=1.25)
                    case "Claim pregnancy": make_slide("mccarthy.jpg", "1950s Outcome: Temporary reprieve. Put under FBI surveillance until 'proof' emerges.", a=1.25, b=1.25)
                    case "Name accusers": make_slide("mccarthy.jpg", "1950s Outcome: Countersuit backfires. labeled 'agitator.' Passport revoked.", a=1.25, b=1.25)
            case "Plead Fifth":
                choice3 = make_slide("salem_jail.jpg", "Salem: They call your silence Satan's work. Jailers test your faith. React?", ["Recite Lord's Prayer", "Spit communion wine", "Fake possession", "Beg for bread"])
                match choice3:
                    case "Recite Lord's Prayer": make_slide("mccarthy.jpg", "1950s Outcome: 'Fifth = guilt!' headlines. Career over, house vandalized.", a=1.25, b=1.25)
                    case "Spit communion wine": make_slide("mccarthy.jpg", "1950s Outcome: Expelled from union. Can't work legally again.", a=1.25, b=1.25)
                    case "Fake possession": make_slide("mccarthy.jpg", "1950s Outcome: Committed for CIA 'deprogramming' experiments.", a=1.25, b=1.25)
                    case "Beg for bread": make_slide("mccarthy.jpg", "1950s Outcome: Broken. Become informant naming old friends.", a=1.25, b=1.25)
            case "Name colleagues":
                choice3 = make_slide("salem_spectral.jpg", "Salem: You name others. They demand spectral evidence. Provide?", ["Bring poppet", "Point at shadow", "Weep on Bible", "Refuse")
                match choice3:
                    case "Bring poppet": make_slide("evidence.jpg", "1950s Outcome: Forged letters 'prove' your claims. Keep your job... for now.")
                    case "Point at shadow": make_slide("paranoia.jpg", "1950s Outcome: Your accusations spark office purges. Promoted through fear.")
                    case "Weep on Bible": make_slide("redeemer.jpg", "1950s Outcome: Hailed as patriot. Made to testify at 20+ hearings.")
                    case "Refuse": make_slide("uncooperative.jpg", "1950s Outcome: Marked 'unreliable.' Quietly erased from industry records.")
            case "Accuse committee":
                choice3 = make_slide("salem_judge.jpg", "Salem: You accuse the judge of witchcraft. Chaos erupts. Respond?", ["Present 'proof'", "Demand trial by water", "Recant", "Flee"])
                match choice3:
                    case "Present 'proof'": make_slide("censure.jpg", "1950s Outcome: Congress censures you. Live under constant IRS audit.")
                    case "Demand trial by water": make_slide("defiant.jpg", "1950s Outcome: Branded 'dangerous radical.' Serve 3 years in Alcatraz.")
                    case "Recant": make_slide("retraction.jpg", "1950s Outcome: Forced retraction printed. Nobody believes it.")
                    case "Flee": make_slide("defect.jpg", "1950s Outcome: Escape to Mexico. Rumored communist defection follows you.")

    case "False confession":
        choice2 = make_slide("red_chanel.jpg", "1951: You admit past Party ties to save career. 'Name names!' reporters shout.", ["Name actors", "Name writers", "Fake amnesia", "Blame spouse"])
        match choice2:
            case "Name actors":
                choice3 = make_slide("salem_poppet.jpg", "Salem: They find a poppet in your home. 'Explain this!'", ["Blame child", "Say it's doll", "Accuse enemy", "Claim hysteria"])
                match choice3:
                    case "Blame child": make_slide("custody.jpg", "1950s Outcome: Child taken by state. Become anti-red poster parent.")
                    case "Say it's doll": make_slide("proof.jpg", "1950s Outcome: Photos surface 'proving' Kremlin visits. Perjury charges.")
                    case "Accuse enemy": make_slide("revenge.jpg", "1950s Outcome: Target sues for libel. Lose life savings in court.")
                    case "Claim hysteria": make_slide("electroshock.jpg", "1950s Outcome: Committed. Endure 'patriotic re-education' therapy.")
            case "Name writers":
                choice3 = make_slide("salem_book.jpg", "Salem: Your foreign books are evidence. Last defense?", ["Deny ownership", "Claim ignorance", "Burn them", "Quote passages"])
                match choice3:
                    case "Deny ownership": make_slide("fingerprints.jpg", "1950s Outcome: 'Your fingerprints!' headlines. Perjury indictment.")
                    case "Claim ignorance": make_slide("illiteracy.jpg", "1950s Outcome: Play dumb. Forced into humiliating literacy test broadcasts.")
                    case "Burn them": make_slide("bonfire.jpg", "1950s Outcome: Public book burning photo op. Never work in academia again.")
                    case "Quote passages": make_slide("manifesto.jpg", "1950s Outcome: Quotes used as 'proof' of subversion. Grand jury subpoena.")
            case "Fake amnesia":
                choice3 = make_slide("salem_faint.jpg", "Salem: You collapse claiming bewitchment. They...", ["Dunk you", "Check for marks", "Isolate", "Pray over you"])
                match choice3:
                    case "Dunk you": make_slide("waterboard.jpg", "1950s Outcome: 'Enhanced interrogation' reveals 'forgotten' details.")
                    case "Check for marks": make_slide("mole.jpg", "1950s Outcome: Birthmark called 'Soviet microfilm stash scar' by tabloids.")
                    case "Isolate": make_slide("solitary.jpg", "1950s Outcome: 18 months solitary confinement. Emerge broken.")
                    case "Pray over you": make_slide("convert.jpg", "1950s Outcome: Televised baptism into McCarthy's church. Career rebounds.")
            case "Blame spouse":
                choice3 = make_slide("salem_divorce.jpg", "Salem: Your husband supports your accusers. Last move?", ["Claim love", "Accuse him", "Beg mercy", "Curse bloodline"])
                match choice3:
                    case "Claim love": make_slide("divorce.jpg", "1950s Outcome: Quick divorce. Ex testifies against you in custody battle.")
                    case "Accuse him": make_slide("alienation.jpg", "1950s Outcome: Children denounce you. Die alone in boarding house.")
                    case "Beg mercy": make_slide("pardon.jpg", "1950s Outcome: Conditional pardon requires testifying against union allies.")
                    case "Curse bloodline": make_slide("legacy.jpg", "1950s Outcome: Family changes name. Gravesite vandalized for decades.")
    case "Stay silent":
        choice2 = make_slide("committee_hearing.jpg", "1954: You invoke the Fifth Amendment. The committee threatens your friends’ careers.", ["Testify to protect them", "Stay silent", "Flee to Canada", "Demand counsel"])
        match choice2:
            case "Testify to protect them":
                choice3 = make_slide("salem_friends.jpg", "Salem: To save your friends, you speak — but your voice cracks. The crowd mutters.", ["Blame the Devil", "Name a widow", "Claim illness", "Collapse"])
                match choice3:
                    case "Blame the Devil": make_slide("brainwash.jpg", "1950s Outcome: Branded ‘brainwashed.’ Forced into televised ‘deprogramming.’")
                    case "Name a widow": make_slide("scandal.jpg", "1950s Outcome: Widow sues for defamation. Your testimony aired endlessly.")
                    case "Claim illness": make_slide("quarantine.jpg", "1950s Outcome: Declared ‘security risk.’ Job terminated, medical license revoked.")
                    case "Collapse": make_slide("weakness.jpg", "1950s Outcome: ‘Weakness proves guilt!’ headlines. Neighbors shun your family.")
            case "Stay silent":
                choice3 = make_slide("salem_cell.jpg", "Salem: You rot in jail. The magistrate offers one last deal: confess or hang.", ["Confess falsely", "Stay defiant", "Bribe guard", "Write confession"])
                match choice3:
                    case "Confess falsely": make_slide("recant.jpg", "1950s Outcome: Forced to recant on radio. Still added to Hollywood blacklist.")
                    case "Stay defiant": make_slide("alcatraz.jpg", "1950s Outcome: Held in contempt. Sent to federal prison for ‘sedition.’")
                    case "Bribe guard": make_slide("corruption.jpg", "1950s Outcome: Bribe discovered. Indicted on 12 counts. Die mid-trial.")
                    case "Write confession": make_slide("memoir.jpg", "1950s Outcome: ‘Confession’ becomes bestseller. Proceeds seized by the state.")
            case "Flee to Canada":
                choice3 = make_slide("salem_forest.jpg", "Salem: You flee into the woods. A hunter tracks you. Do you...?", ["Hide in a barn", "Fight him", "Surrender", "Pray for fog"])
                match choice3:
                    case "Hide in a barn": make_slide("defector.jpg", "1950s Outcome: Labeled defector. FBI interrogates family for years.")
                    case "Fight him": make_slide("violence.jpg", "1950s Outcome: ‘Violent tendencies’ leaked. Added to FBI’s Most Wanted.")
                    case "Surrender": make_slide("traitor.jpg", "1950s Outcome: Extradited. Trial becomes McCarthy’s propaganda victory.")
                    case "Pray for fog": make_slide("exile.jpg", "1950s Outcome: Disappear. Rumored to lecture in Moscow, mocking America.")
            case "Demand counsel":
                choice3 = make_slide("salem_lawyer.jpg", "Salem: ‘Lawyers defend only the guilty!’ they shout. You...", ["Quote English law", "Insist on rights", "Attack the clerk", "Apologize"])
                match choice3:
                    case "Quote English law": make_slide("unamerican.jpg", "1950s Outcome: ‘Foreign influence!’ accusation. Citizenship questioned.")
                    case "Insist on rights": make_slide("dissenter.jpg", "1950s Outcome: ‘Rights = Communism!’ Jailed without trial for 2 years.")
                    case "Attack the clerk": make_slide("brutality.jpg", "1950s Outcome: Beaten ‘resisting arrest.’ Left crippled, unemployed.")
                    case "Apologize": make_slide("subservient.jpg", "1950s Outcome: Groveling apology aired. Hired as McCarthy’s janitor.")

    case "Blame someone else":
        choice2 = make_slide("press_conference.jpg", "1950: You accuse a rival of communist ties. Cameras flash as they’s dragged away.", ["Double down", "Retract", "Claim FBI pressured you", "Smirk"])
        match choice2:
            case "Double down":
                choice3 = make_slide("salem_wheel.jpg", "Salem: The court demands more names. The wheel of blame turns. You...", ["Name enemies", "Refuse", "Fake a vision", "Accuse the governor"])
                match choice3:
                    case "Name enemies": make_slide("informant.jpg", "1950s Outcome: Promoted to FBI informant. Live in safehouses, despised.")
                    case "Refuse": make_slide("turncoat.jpg", "1950s Outcome: ‘Turncoat!’ Former allies leak your secrets. Disappear.")
                    case "Fake a vision": make_slide("propaganda.jpg", "1950s Outcome: Star in anti-commie films. Win Oscar. Hate yourself.")
                    case "Accuse the governor": make_slide("treason.jpg", "1950s Outcome: Indicted for treason. Die of ‘heart attack’ in custody.")
            case "Retract":
                choice3 = make_slide("salem_recant.jpg", "Salem: You take it back. The crowd hisses. ‘Liar!’ they scream. You...", ["Weep", "Blame the Devil", "Attack accuser", "Faint"])
                match choice3:
                    case "Weep": make_slide("pity.jpg", "1950s Outcome: Tearful TV plea fails. Eggs thrown at your house nightly.")
                    case "Blame the Devil": make_slide("exorcist.jpg", "1950s Outcome: Church ‘exorcises’ you on live TV. Become a punchline.")
                    case "Attack accuser": make_slide("violence2.jpg", "1950s Outcome: Charged with assault. Cellmate ‘accidentally’ kills you.")
                    case "Faint": make_slide("incompetent.jpg", "1950s Outcome: Deemed mentally unfit. Estate controlled by the state.")
            case "Claim FBI pressured you":
                choice3 = make_slide("salem_spectral.jpg", "Salem: ‘A specter made me do it!’ you cry. The court...", ["Demands proof", "Tortures you", "Laughs", "Burns your home"])
                match choice3:
                    case "Demands proof": make_slide("wiretap.jpg", "1950s Outcome: FBI releases edited tapes ‘proving’ your cooperation.")
                    case "Tortures you": make_slide("mkultra2.jpg", "1950s Outcome: Disappear into CIA program. Family told you ‘defected.’")
                    case "Laughs": make_slide("ridicule.jpg", "1950s Outcome: Satirized in papers. Die penniless in flophouse.")
                    case "Burns your home": make_slide("arson.jpg", "1950s Outcome: House burns. Fire marshal blames ‘commie agitators.’")
            case "Smirk":
                choice3 = make_slide("salem_smug.jpg", "Salem: You smirk as others hang. The crowd notices. They...", ["Riot", "Cheer", "Stone you", "Demand more trials"])
                match choice3:
                    case "Riot": make_slide("chaos.jpg", "1950s Outcome: Media calls you ‘instigator.’ Banned from all broadcasts.")
                    case "Cheer": make_slide("celebrity.jpg", "1950s Outcome: Fame as ‘patriot.’ Later exposed as fraud. Suicide.")
                    case "Stone you": make_slide("mob.jpg", "1950s Outcome: Ambushed by vigilantes. Cops ‘can’t find’ suspects.")
                    case "Demand more trials": make_slide("witch_hunt.jpg", "1950s Outcome: Praised by McCarthy. Given show trial producer role.")