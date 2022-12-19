var district_arr = new Array("Ahmedabad","Amreli","Anand","Aravalli","Banaskantha","Bharuch","Bhavnagar","Botad","Chhota Udepur","Dahod","Dang","Devbhoomi Dwarka","Gandhinagar","Gir Somnath","Jamnagar","Junagadh","Kachchh","Kheda","Mahisagar","Mehsana","Morbi","Narmada","Navsari","Panchmahal","Patan","Porbandar","Rajkot","Sabarkantha","Surat","Surendranagar","Tapi","Vadodara","Valsad");

var d_t = new Array();
d_t[0]="";
d_t[1]=" City East | City West | Bavla | Daskroi | Detroj-Rampura | Dhandhuka | Dholera | Dholka | Mandal | Sanand | Viramgam ";
d_t[2]=" Amreli | Babra | Bagasara | Dhari | Jafrabad | Khambha | Kunkavav | vadia | Lathi | Lilia | Rajula | Savarkundla ";
d_t[3]=" Anand | Anklav | Borsad | Khambhat | Petlad | Sojitra | Tarapur | Umreth ";
d_t[4]=" Bayad | Bhiloda | Dhansura | Malpur | Meghraj | Modasa ";
d_t[5]=" Amirgadh | Bhabhar | Danta | Dantiwada | Deesa | Deodar | Dhanera | Kankrej | Lakhani | Palanpur | Suigam | Tharad | Vadgam | Vav ";
d_t[6]=" Bharuch | Amod | Ankleshwar | Hansot | Jambusar | Jhagadia | Netrang | Vagra | Valia ";
d_t[7]=" Bhavnagar | Gariadhar | Ghogha | Jesar | Mahuva | Palitana | Sihor | Talaja | Umrala | Vallabhipur ";
d_t[8]=" Botad | Barwala | Gadhada | Ranpur ";
d_t[9]=" Chhota Udepur | Bodeli | Jetpur pavi | Kavant | Nasvadi | Sankheda ";
d_t[10]=" Dahod | Devgadh baria | Dhanpur | Fatepura | Garbada | Limkheda | Sanjeli | Jhalod ";
d_t[11]=" Ahwa | Subir | Waghai ";
d_t[12]=" Bhanvad | Kalyanpur | Khambhalia | Okhamandal ";
d_t[13]=" Gandhinagar |Dehgam |Kalol |Mansa ";
d_t[14]=" Gir Gadhda | Kodinar | Veraval | Sutrapada | Talala | Una ";
d_t[15]=" Jamnagar | Dhrol | Jamjodhpur | Jodiya | Kalavad | Lalpur ";
d_t[16]=" Junagadh taluka | Bhesana | Junagadh Rural | Keshod | Malia | Manavadar | Mangrol | Mendarda | Vanthali | Visavadar ";
d_t[17]=" Abdasa | Anjar | Bhachau | Bhuj | Gandhidham | Lakhpat | Mandvi | Mundra | Nakhatrana | Rapar ";
d_t[18]=" Kheda | Galteshwar | Kapadvanj | Kathlal | Mahudha | Matar | Mehmedabad | Nadiad | Thasra | Vaso ";
d_t[19]=" Balasinor | Kadana | Khanpur | Lunawada | Santrampur | Virpur ";
d_t[20]=" Mehsana | Becharaji | Jotana | Kadi | Kheralu | Satlasana | Unjha | Vadnagar | Vijapur | Visnagar ";
d_t[21]=" Halvad | Maliya | Morbi | Tankara | Wankaner ";
d_t[22]=" Dediapada | Garudeshwar | Nandod | Sagbara | Tilakwada ";
d_t[23]=" Navsari | Vansda | Chikhli | Gandevi | Jalalpore | Khergam ";
d_t[24]=" Ghoghamba | Godhra | Halol | Jambughoda | Kalol | Morwa Hadaf | Shehera ";
d_t[25]=" Patan | Chanasma | Harij | Radhanpur | Sami | Sankheswar | Santalpur | Sarasvati | Sidhpur ";
d_t[26]=" Porbandar | Kutiyana | Ranavav ";
d_t[27]=" Rajkot | Dhoraji | Gondal | Jamkandorna | Jasdan | Jetpur | Kotada Sangani | Lodhika | Paddhari | Upleta | Vinchchiya ";
d_t[28]=" Himatnagar | Idar | Khedbrahma | Poshina | Prantij | Talod | Vadali | Vijaynagar ";
d_t[29]=" Surat | Bardoli | Choryasi | Kamrej | Mahuva | Mandvi | Mangrol | Olpad | Palsana | Umarpada ";
d_t[30]=" Chotila | Chuda | Dasada | Dhrangadhra | Lakhtar | Limbdi | Muli | Sayla | Thangadh | Wadhwan ";
d_t[31]=" Nizar | Songadh | Uchchhal | Valod | Vyara | Kukurmunda ";
d_t[32]=" Vadodara | Dabhoi | Desar | Karjan | Padra | Savli | Sinor | Vaghodia ";
d_t[33]=" Valsad | Dharampur | Kaprada | Pardi | Umbergaon | Vapi ";

function print_district(district_id){
	// given the id of the <select> tag as function argument, it inserts <option> tags
	var option_str = document.getElementById(district_id);
	option_str.length=0;
	option_str.options[0] = new Option('Select district','');
	option_str.selectedIndex = 0;
	for (var i=0; i<district_arr.length; i++) {
		option_str.options[option_str.length] = new Option(district_arr[i],district_arr[i]);
	}
}


function print_taluka(taluka_id, taluka_index){
	var option_str = document.getElementById(taluka_id);
	option_str.length=0;	// Fixed by Julian Woods
	option_str.options[0] = new Option('Select taluka','');
	option_str.selectedIndex = 0;
	var taluka_arr = d_t[taluka_index].split("|");
	for (var i=0; i<taluka_arr.length; i++) {
		option_str.options[option_str.length] = new Option(taluka_arr[i],taluka_arr[i]);
	}
}
