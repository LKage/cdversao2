var Programa = Programa || {};


Programa.MaskCep = (function() {

	function MaskCep() {
		this.inputCep = $('.js-cep');
	}

	MaskCep.prototype.enable = function() {
		this.inputCep.mask('00.000-000');
	}

	return MaskCep;

}());

Programa.MaskDate = (function() {

	function MaskDate() {
		this.inputDate = $('.js-date');
	}

	MaskDate.prototype.enable = function() {
		this.inputDate.mask('00/00/0000');
		this.inputDate.datepicker({
			orientation: 'auto',
			language: 'pt-BR',
			autoclose: true,
			todayHighlight: true
		});
	}

	return MaskDate;

}());

$(function() {
	var maskDate = new Programa.MaskDate();
	maskDate.enable();

	var maskCep = new Programa.MaskCep();
	maskCep.enable();
});
