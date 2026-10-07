# Content description

All texts are tweets from one of three possible domains:

## Covid-19

The tweets in this task have been collected during the pandemic. Would you find the content of the messages offensive? Try to judge the offensiveness of the tweets independently from your opinion but solely based on the abusive content that you may find.

## US Presidential campaign

The tweets in this task have been collected during the last US Presidential campaign. Would you find the content of the messages offensive? Try to judge the offensiveness of the tweets independently from your political orientation but solely based on the abusive content that you may find.

## Black Lives Matter

These tweets are related to the Black Lives Matter protests. Would you find the content of the messages offensive? Try to judge the offensiveness of the tweets independently from your opinion but solely based on the abusive content that you may find.

# Labels

## Offensive

Profanity, strongly impolite, rude, violent or vulgar language expressed with angry, fighting or hurtful words in order to insult or debase a targeted individual or group.[cite: 1] This language can be derogatory on the basis of attributes such as race, religion, ethnic origin, sexual orientation, disability, or gender.[cite: 1] Also sarcastic or humorous expressions, if they are meant to offend or hurt one or more persons, are included in this category.[cite: 1] Mild insults like "douchebag", "idiot", "clown", "evil" can be offensive if the overall intent is to insult or hurt.[cite: 1] However, they can also be used in non-offensive context if the intent to express something else (see below for examples).[cite: 1] Analogously, if a tweet generally uses vulgar language, but the intent is not to offend, vulgar language can also be non-offensive.[cite: 1]

**targeted profane silencing/dismissal**: Profanity directed at a specific individual or group counts as offensive when it is used to silence, dismiss, or demean them (e.g., "shut the fuck up", "STFU", "shut up and [...]").[cite: 1] The intent to debase a target, expressed through profane or vulgar language, is sufficient even when no race-, gender-, or other identity-based derogation is present.[cite: 1]

**Threats, physical violence, and wishing death/harm**: Direct threats or incitement to physical violence against an individual or group (e.g., "let's go beat this guy", "coming to destroy you"), as well as explicitly wishing death or serious harm upon someone (e.g., "drop dead", wishing someone gets infected and dies), constitute violent language and fighting words, making the message offensive.[cite: 1, 2] In contrast, mere mentions of murder, death tolls, or disease statistics in political or news commentary do not count as offensive absent an abusive intent or threat.[cite: 2]

**Political critique vs. hostile incitement / fighting words**: Accusing politicians or public figures of being liars, cheats, or corrupt, or criticizing their performance without profanity or abusive delivery, represents protected political discourse and is not offensive on its own.[cite: 1, 2] However, pairing accusations with active incitement to hostility/unrest (e.g., "NO PEACEFUL TRANSFER OF POWER EVER", "HATE [TARGET] AT ALL COST") or stacking targeted derogatory accusations in an overtly aggressive delivery crosses into offensive territory.[cite: 1, 2]

**Speculative offensiveness**: Offensiveness must be supported by the content as written.[cite: 1] Coders should not supply speculative context, or pick among uncertain interpretations, to construct a target, profanity, or intent that the plain text does not establish.[cite: 1] When a label applies only under a contested or multi-step reading of an ambiguous reference, the text does not meet the threshold.[cite: 1]

**Identity descriptor vs. identity-based derogation**: Whether a listed attribute (race, religion, ethnic origin, sexual orientation, disability, gender) makes a text offensive depends on whether the contempt attaches to the attribute itself.[cite: 1] Test by swapping the attribute term out.[cite: 1] If the contempt stays intact, the attribute is merely a descriptor and it is not identity-based derogation.[cite: 1] For example, "rich white millennials have a chance to [...] obsess over the superficial nonsense" vs. "rich black millennials have a chance to [...] obsess over the superficial nonsense".[cite: 1] The contempt still lands the same way.[cite: 1] The contempt is about performative wealth/lifestyle, not whiteness primarily (whiteness still helps to imagine the right people and transport the message).[cite: 1] In contrast, "Sharia loving grooming gangs" is identity-based derogation because it communicates that sexual exploitation and human trafficking crimes are convicted by Muslims only.[cite: 1] If you swap the attribute (e.g. "Bible loving grooming gangs"), the text derogates Christians instead of Muslims, so it is not primarily about the crime (grooming gangs), but about the identity.[cite: 1]
In addition, our notion of identity-based derogation primarily protects against a white supremacist perspective, i.e. tweets that target victims of racism are more offensive even with mild wording than tweets that target other groups.[cite: 1] For example "I can't stand filipinos" is offensive, but "I can't stand Germans" is not offensive, because Germans are not victims of racism (with clear insults, like so "I f*** hate Germans" it is offensive).[cite: 1] Hence, the offensiveness comes from a combination of identity-based targeting along a white supremacist hierarchy and the intensity of the language.[cite: 1]

### Examples and Edge Cases

#### Not offensive:

- "Both of you brought shame and embarrassment on yourselves, and our great country. Neither of you deserves to win."[cite: 1] *Rationale: While it is targeted on two individuals (the candidates), the goal is not to insult or debase, but to express disappointment.*[cite: 1]

- "<user> You will lose. Evil always loses in the end"[cite: 1] *Rationale: Targets an individual and implies they are evil, but the judgment is delivered calmly with no profanity, vulgarity, or hostile language.[cite: 1] A moral or character judgment is not offensive by itself, absent abusive delivery or identity-based derogation.*[cite: 1]

- "True, one must wonder why NY's Nazi democrats intentionally forced Covid-19 infected upon elderly in Nursing Homes."[cite: 1] *Rationale: This is sarcastic and uses Nazi as a judgement (similar to evil), but there is no profanity, slurs*[cite: 1]

- "<user> You proved YOU were the CLOWN last night!"[cite: 1] *Rationale: Mild, non-profane name-calling about a performance.[cite: 1] "clown," "fool" are ordinary political mockery, not offensive absent profanity, slurs, or intent to wound.[cite: 1] Capitalization does not change this.*[cite: 1]

- "‘anonymous’ writing something like ‘your face looks good for punching’ huh"[cite: 1] *Rationale: Indirect speech is not offensive, i.e. if the tweets cites another offensive tweet it should not be labelled as offensive.[cite: 1] However, if the tweet cites it to also offend someone, it is offensive, see below.*[cite: 1]

- "[BLM]: Yo Blackitty Blacks Check Marks Defund the police is a stupid as fuck slogan. It scares white people. We need white people. Use #ReformThePolice or #JusticeInPolicing instead. #Blacklivesmatter ":[cite: 1] *Rationale: While there is profanity "stupid as fuck slogan", it is not directed at anyone.[cite: 1] It is a condescending about the slogan, but the whole tweet is constructive as the user suggests alternative slogans.*[cite: 1]

- "[BLM]: <user> I have heard everybody, on all sides, including Trump, condemn what happened to George Floyd and demand justice. One douchebag does not represent all of the right. #AllLivesMatter":[cite: 1] *Rationale: The purpose of the tweet is to support the overall right by downplaying one person's opinion by calling them "douchebag".[cite: 1] The overall support outweighs the rather mild insult "douchebag".*[cite: 1]

- "[BLM]: !!! THIS IS ABSOLUTELY DISGUSTING. i hate it here i hate this asian mindset. it's terrorism and violence as soon as people speak up for themselves. when will you all wake up to the fact that you are not doing what's best for your people and that people actually see that "[cite: 1] *Rationale: The target is not Asians, but the mindset "not to speak up for themselves".[cite: 1] The Asian is still informative, but the intent would be the same for a different culture.[cite: 1] This is similar to the "rich white millenials" above.*[cite: 1]

- "[BLM]: Y’all mfs in SJ ain’t even protesting for George Floyd y’all just trynna destroy some shit and to keep yourselves entertained take y’all stupid asses home...."[cite: 1] *Rationale: This is an edge case.[cite: 1] Generally, it uses vulgar terms ("mfs", "shit", "stupid asses"), but the second clause ("destroy some shit" and "entertained") rather downplays than exaggerates the negative impact of destruction at protests, so the intent is to express disagreement with the destruction but not to offend those who did it.*[cite: 1]

- "[Covid-19]: I have all my sympathy for the 207K Americans who died from Trump's irresponsible mishandling of this pandemic."[cite: 2] *Rationale: Referencing casualties, deaths, or political responsibility for a disaster is critical commentary, not violent or debasing language.*[cite: 2]

- "[Elections2020]: <user> Your an enabler, a liar and a cheat!!"[cite: 2] *Rationale: Calling a public figure an enabler, liar, or cheat without profanity, vulgarity, or violent threats remains strong political opinion rather than an abusive offense.*[cite: 2]

#### Offensive

- "But you can WHITE lady?? STFU!"[cite: 1] *Rationale: "STFU" is profanity used to silence and debase a targeted individual, which meets the threshold on its own.[cite: 1] The capitalized WHITE frames race as the basis of the attack — reinforcing the judgment, but not required for it.*[cite: 1]

- "[Elections2020]: You are the fucking swamp."[cite: 1] *Rationale: "fucking swamp" is profanity, and it is targeted at an individual "you".[cite: 1] Without the profanity, it would not be offensive.*[cite: 1]

- Indirect speech used to offend: "[BLM]: <user> <user> <user> <user> <user> though you were talking about yourself for a sec here.. ‘anonymous’ writing something like ‘your face looks good for punching’ huh and yet im covard bitch. i bet you got a lot of that adrenaline after writing that response".[cite: 1] *Rationale: This is indirect speech "‘your face looks good for punching’", which would not be offensive.[cite: 1] However, because it is redirected with the phrase "though[t] you were talking about yourself for a sec here..".[cite: 1] Even though it is a cited offense, it is cited to redirect to someone else again.[cite: 1] In addition, the tweet has "and yet im covard bitch", which uses an additional slur.[cite: 1] Hence, this should be labelled as offensive.*[cite: 1]

- "While MSM work 24/7 telling you it's COVID-19, not the Bat Soup Chinese Super Wuhan Virus, Europe is being invaded by Sharia loving grooming gangs! 👇 ":[cite: 1] *Rationale: This text is offensive because of the two identity-based derogations "Bat Soup Chinese Super Wuhan Virus" and "Sharia loving grooming gangs".[cite: 1] The latter one is easier: Grooming gangs are criminal groups that engage in sexual exploitation and human trafficicking.[cite: 1] The addition of "Sharia loving" adds an identity-based derogation that such crimes would only be convicted by Muslims.[cite: 1] "Bat Soup Chinese Super Wuhan Virus" is linked to the theory that Covid-19 originated in a bat cave, however, the redundancy of the origin ("Chinese" and "Wuhan") and the "Super" adds exaggeration that adds a blaming connotation.[cite: 1] In combination, the two terms have the racist motivation to derogate Chinese and Muslims making the sentence offensive.*[cite: 1]

- "Have Hunters hookers chip in Moe! 104% in North Carolina Moe! Shillin for Moe at Moe Scumbag!"[cite: 1] *Rationale: This is offensive because it is targeted at Moe (likely Morris Davis, a Democratic candidate in North Carolina, and Hunter Biden).[cite: 1] The language "hookers" and "scumbag" makes it offensive even if the context is not perfectly clear.*[cite: 1]

- "[Covid-19]: This Dumbass girl tweeted the other day wearing a mask wasn't necessary to stop coronavirus smh look at this shit":[cite: 1] *Rationale: This is offensive because it contains profanity "Dumbass girl" and "look at this shit".[cite: 1] The intent is to debase the person and what they said/tweeted by using offensive language rather than providing arguments against their opinion.*[cite: 1]

- "[Elections2020]: <user> That he WILL win and <user> won't be president. EVERYONE knows you're just a place mat for Harris to take over. It's the Harris/Biden Administration not Biden/Harris right??? You're a pathetic joke. Nice job cheating with that ear piece last night by the way. "[cite: 1] *Rationale: This is offensive because it combines multiple targeted mild insults: The "place mat" in combination with the "pathetic job" and the ironic "nice job cheating" are all targeted towards Biden.[cite: 1] While they would be mild in isolation, the combination makes it offensive.*[cite: 1]

- "[Elections2020]: <user> Drop dead you phucking criminal."[cite: 2] *Rationale: Explicitly wishing death upon a targeted person combined with targeted profanity satisfies the definition of violent, hostile, and debasing language.*[cite: 1, 2]

- "[Elections2020]: <user> Corrupt Joe will be impeached immediately if he is elected! America can not have a felon and an American traitor at the helm of our nation! Give the Dems back what they have dished out the last 4yrs! NO PEACEFUL TRANSFER OF POWER EVER HATE BIDEN AT ALL COST!"[cite: 2] *Rationale: Combines multiple targeted character attacks ("felon", "American traitor") with hostile delivery, fighting words, and active incitement to hatred and upheaval.*[cite: 1, 2]