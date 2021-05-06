# Generated by Django 3.1.5 on 2021-05-06 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0002_auto_20210419_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='regiao',
            field=models.CharField(choices=[('AC', 'Águas Claras'), ('AS', 'Asa Sul'), ('AN', 'Asa Norte'), ('AR', 'Arniqueira'), ('BZ', 'Brazilandia'), ('CA', 'Candangolândia'), ('CI', 'Ceilândia'), ('CZ', 'Cruzeiro'), ('FE', 'Fercal'), ('GA', 'Gama'), ('GR', 'Guará'), ('IT', 'Itapoã'), ('JB', 'Jardim Botânico'), ('LS', 'Lago Sul'), ('LN', 'Lago Norte'), ('NB', 'Núcleo Bandeirante'), ('PW', 'Park Way'), ('PA', 'Paranoá'), ('PL', 'Planaltina'), ('PP', 'Plano Piloto'), ('RE', 'Recanto das Emas'), ('RF', 'Riacho Fundo'), ('SA', 'Samambaia'), ('SM', 'Santa Maria'), ('SB', 'São Sabastião'), ('SCIA', 'SCIA'), ('RF', 'Riacho Fundo'), ('RFII', 'Riacho Fundo II'), ('SI', 'SIA'), ('SO', 'Sobradinho'), ('SOII', 'Sobradinho II'), ('SN', 'Sol Nascente'), ('SD', 'Sudoeste'), ('TA', 'Taguatinga'), ('VA', 'Varjão'), ('VP', 'Vicente Pires'), ('EO', 'Entre outros')], max_length=4),
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('data', models.DateField(auto_now_add=True)),
                ('problemasPessoais', models.IntegerField(choices=[(-1, 'Pior que antes'), (0, 'Sem mudança'), (1, 'Melhor que antes')], default=True)),
                ('humor', models.IntegerField(choices=[(-1, 'Pior que antes'), (0, 'Sem mudança'), (1, 'Melhor que antes')], default=False)),
                ('estabilidadeDeEmoções', models.IntegerField(choices=[(-1, 'Pior que antes'), (0, 'Sem mudança'), (1, 'Melhor que antes')], default=False)),
                ('interessePelaVida', models.IntegerField(choices=[(-1, 'Pior que antes'), (0, 'Sem mudança'), (1, 'Melhor que antes')], default=False)),
                ('capacidadeDeSituaçõesDificeis', models.IntegerField(choices=[(-1, 'Pior que antes'), (0, 'Sem mudança'), (1, 'Melhor que antes')], default=False)),
                ('convivioFamiliar', models.IntegerField(choices=[(-1, 'Pior que antes'), (0, 'Sem mudança'), (1, 'Melhor que antes')], default=False)),
                ('energiaSono', models.IntegerField(choices=[(-1, 'Pior que antes'), (0, 'Sem mudança'), (1, 'Melhor que antes')], default=False)),
                ('convivioAmigos', models.IntegerField(choices=[(-1, 'Pior que antes'), (0, 'Sem mudança'), (1, 'Melhor que antes')], default=False)),
                ('conhecimentoDoenca', models.IntegerField(choices=[(-1, 'Pior que antes'), (0, 'Sem mudança'), (1, 'Melhor que antes')], default=False)),
                ('criseEspaçoInterior', models.IntegerField(choices=[(-1, 'Pior que antes'), (0, 'Sem mudança'), (1, 'Melhor que antes')], default=False)),
                ('exposiçãoRisco', models.IntegerField(choices=[(-1, 'Pior que antes'), (0, 'Sem mudança'), (1, 'Melhor que antes')], default=False)),
                ('qualidadeSono', models.IntegerField(choices=[(-1, 'Pior que antes'), (0, 'Sem mudança'), (1, 'Melhor que antes')], default=False)),
                ('tentativaSuicidio', models.IntegerField(choices=[(-1, 'Pior que antes'), (0, 'Sem mudança'), (1, 'Melhor que antes')], default=False)),
                ('qualidadeEscuta', models.IntegerField(choices=[(-1, 'Pior que antes'), (0, 'Sem mudança'), (1, 'Melhor que antes')], default=False)),
                ('maturidadeEmocional', models.IntegerField(choices=[(-1, 'Pior que antes'), (0, 'Sem mudança'), (1, 'Melhor que antes')], default=False)),
                ('qualidadeNutritiva', models.IntegerField(choices=[(-1, 'Pior que antes'), (0, 'Sem mudança'), (1, 'Melhor que antes')], default=False)),
                ('autoMedicacao', models.IntegerField(choices=[(-1, 'Pior que antes'), (0, 'Sem mudança'), (1, 'Melhor que antes')], default=False)),
                ('intoleranciaFrustração', models.IntegerField(choices=[(-1, 'Pior que antes'), (0, 'Sem mudança'), (1, 'Melhor que antes')], default=False)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paciente.paciente')),
            ],
        ),
    ]
